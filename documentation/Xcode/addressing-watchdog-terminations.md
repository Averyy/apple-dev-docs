# Addressing watchdog terminations

**Framework**: Xcode

Identify the signature of an unresponsive app terminated by the watchdog, and address the issue.

#### Overview

Users expect apps to launch quickly, and are responsive to touches and gestures. The operating system employs a watchdog that monitors launch times and app responsiveness, and terminates unresponsive apps. Watchdog terminations use the code `0x8badf00d` (pronounced “ate bad food”) in the Termination Reason of a crash report:

```other
Exception Type:  EXC_CRASH (SIGKILL)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note:  EXC_CORPSE_NOTIFY
Termination Reason: Namespace SPRINGBOARD, Code 0x8badf00d
```

The watchdog terminates apps that block the main thread for a significant time. There are many ways to block the main thread for an extended time, such as:

- Synchronous networking
- Processing large amouts of data, such as large JSON files or 3D models
- Triggering lightweight migration for a large [`Core Data`](https://developer.apple.com/documentation/CoreData) store synchronously
- Analysis requests with [`Vision`](https://developer.apple.com/documentation/Vision)

To understand why blocking the main thread is an issue, consider the most common example, loading data into the UI from a synchronous network call. If the main thread is busy with a network request, the system can’t handle UI events, such as multiple scroll events, until after completing the network call. If the network call takes a long time, there’s a significant time from when the user scrolls to when the app responds to the scroll events. This makes the app feel unresponsive.

![A timing diagram for the main thread showing UI scrolling events queued behind a long-running networking operation.](https://docs-assets.developer.apple.com/published/9358acb2a74668e16ec2237d70a571f5/addressing-watchdog-terminations-1%402x.png)

##### Interpret the App Responsiveness Watchdog Information

When an app is slow to launch or respond to events, the termination information in the crash report contains important information about how the app spent its time. For example, an iOS app that doesn’t render the UI quickly after launch has the following in the crash report:

```other
Termination Description: SPRINGBOARD, 
    scene-create watchdog transgression: application<com.example.MyCoolApp>:667
    exhausted real (wall clock) time allowance of 19.97 seconds 
    | ProcessVisibility: Foreground 
    | ProcessState: Running 
    | WatchdogEvent: scene-create 
    | WatchdogVisibility: Foreground 
    | WatchdogCPUStatistics: ( 
    |  "Elapsed total CPU time (seconds): 15.290 (user 15.290, system 0.000), 28% CPU", 
    |  "Elapsed application CPU time (seconds): 0.367, 1% CPU" 
    | )
```

> **Note**: For readability, this example includes extra line breaks. In the original crash report file for this example, the watchdog information is on fewer lines.

When `scene-create` appears in the `Termination Description`, the app didn’t render the first frame of its UI to the screen within the allowed wall clock time. If `scene-update` appears in the `Termination Description` instead of `scene-create`, the app didn’t update its UI quick enough because the main thread is too busy.

> **Note**: The `scene-create` and `scene-update` terminology used in the crash report refers to any content drawn to the device’s screen. This terminology has no relation to [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) in a scene-based [`UIKit`](https://developer.apple.com/documentation/UIKit) app.

The `Elapsed total CPU time` shows how much time the CPU ran for all processes on the system within the wall clock time. This CPU time, as well as the application CPU time, is for the total CPU utilization across CPU cores, which can exceed 100%. For example, if one CPU core is at 100% utilization and a second CPU core is at 20% utilization, the total CPU utalization is 120%.

The `Elapsed application CPU time` shows how much time the app spent running on the CPU within the wall clock time. If this number is at either extreme, it is a hint to the problem. If this number is high, the app is performing significant work across all of its threads—the number aggregates all threads, and isn’t specific to the main thread. If this number is low, the app is mostly idle, because it is waiting on system resources, such as a network connection.

##### Interpret Background Task Watchdog Information Watchos

In addition to the app responsiveness watchdog, watchOS has a watchdog for background tasks. In this example, an app didn’t complete handling a [`Watch Connectivity`](https://developer.apple.com/documentation/WatchConnectivity) background task within the time allowance:

```other
Termination Reason: CAROUSEL, WatchConnectivity watchdog transgression. 
    Exhausted wall time allowance of 15.00 seconds.
Termination Description: SPRINGBOARD,
    CSLHandleBackgroundWCSessionAction watchdog transgression: xpcservice<com.example.MyCoolApp.watchkitapp.watchextension>:220:220 
    exhausted real (wall clock) time allowance of 15.00 seconds 
    | <FBExtensionProcess: 0x16df02a0; xpcservice<com.example.MyCoolApp.watchkitapp.watchextension>:220:220; typeID: com.apple.watchkit> 
      Elapsed total CPU time (seconds): 24.040 (user 24.040, system 0.000), 81% CPU 
    | Elapsed application CPU time (seconds): 1.223, 6% CPU, lastUpdate 2020-01-20 11:56:01 +0000
```

> **Note**: For readability, this example includes extra line breaks. In the original crash report file for this example, the watchdog information is on fewer lines.

Intrepret the information about wall clock time and CPU time as described in [`Interpret the app responsiveness watchdog information`](addressing-watchdog-terminations#Interpret-the-app-responsiveness-watchdog-information.md).

##### Identify the Reason the Watchdog Triggered

The backtraces are sometimes helpful in identifying what is taking so much time on the app’s main thread. For example, if an app uses synchronous networking on the main thread, networking functions are visible in the main thread’s backtrace.

```other
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   libsystem_kernel.dylib            0x00000001c22f8670 semaphore_wait_trap + 8
1   libdispatch.dylib                 0x00000001c2195890 _dispatch_sema4_wait$VARIANT$mp + 24
2   libdispatch.dylib                 0x00000001c2195ed4 _dispatch_semaphore_wait_slow + 140
3   CFNetwork                         0x00000001c57d9d34 CFURLConnectionSendSynchronousRequest + 388
4   CFNetwork                         0x00000001c5753988 +[NSURLConnection sendSynchronousRequest:returningResponse:error:] + 116  + 14728
5   Foundation                        0x00000001c287821c -[NSString initWithContentsOfURL:usedEncoding:error:] + 256
6   libswiftFoundation.dylib          0x00000001f7127284 NSString.__allocating_init+ 680580 (contentsOf:usedEncoding:) + 104
7   libswiftFoundation.dylib          0x00000001f712738c String.init+ 680844 (contentsOf:) + 96
8   MyCoolApp                         0x00000001009d31e0 ViewController.loadData() (in MyCoolApp) (ViewController.swift:21)
```

However, the main thread’s backtrace doesn’t always contain the source of the issue. For example, imagine that your app needs exactly 4 seconds to complete a task out of a total allowed wall clock time of 5 seconds. When the watchdog terminates the app after 5 seconds, the code that took 4 seconds won’t show up in the backtrace because it completed, yet it consumed almost the entire time budget. The crash report instead records the backtrace frames of what the app was doing at the time the watchdog terminated it, even though the recorded backtrace frames aren’t the source of the problem.

You may be able to use the information from all backtraces in the crash report to help identify where you are in the app’s launch process. By working backwards based on this information, you can identify what code already ran to narrow your investigation to that code.

In addition, profile your app’s performance during development to eliminate problems before releasing the app, and monitor the app’s performance after the app is released. [`Reducing your app’s launch time`](reducing-your-app-s-launch-time.md) and [`Improving app responsiveness`](improving-app-responsiveness.md) provide more information on these techniques.

##### Identify Hidden Synchronous Networking Code

Synchronous networking that blocks the main thread and leads to a watchdog termination are sometimes hidden behind abstraction layers that mask the danger. The example backtrace in [`Identify the reason the watchdog triggered`](addressing-watchdog-terminations#Identify-the-reason-the-watchdog-triggered.md) shows the app triggered the synchronous download by calling `init(contentsOf:)` with a `https` URL, in frame 7. This API implicitly makes a synchronous network request before returning from the initializer. Even if this initalizer completed quickly and wasn’t in the crash report, it still can contribute to a watchdog termination. Other classes with an initalizer that takes a URL parameter, such as [`XMLParser`](https://developer.apple.com/documentation/Foundation/XMLParser) and [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), behave in the same way.

Other common examples of hidden synchronous networking include the following:

- [`SCNetworkReachability`](https://developer.apple.com/documentation/SystemConfiguration/scnetworkreachability-g7d), the reachability API, operates synchronously by default. Seemingly innocuous functions like [`SCNetworkReachabilityGetFlags(_:_:)`](https://developer.apple.com/documentation/SystemConfiguration/SCNetworkReachabilityGetFlags(_:_:)) can trigger a termination by the watchdog.
- DNS functions provided by BSD, like `gethostbyname(_:)` and `gethostbyaddr(_:_:_:)`, are never safe to call on the main thread. Functions like `getnameinfo(_:_:_:_:_:_:_:)` and `getaddrinfo(_:_:_:_:)` are only safe if you’re working exclusively with IP addresses and not DNS names (that is, you specify `AI_NUMERICHOST` and `NI_NUMERICHOST`, respectively).

Synchronous networking issues depend a great deal on the network environment. If you always test your app in your office, where network connectivity is good, you’ll never see this type of issue. However, once you start deploying your app to users—who run apps in all sorts of network environments—synchronous networking problems become common. In Xcode, you can simulate adverse network conditions to aid testing your app under the conditions your users encounter. See [`Test under adverse device conditions (iOS)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev308429d42).

##### Move Code Off the Main Thread

Move all long-running code not essential to your app’s UI to a background queue. By moving this work to a background queue, the app’s main thread can complete the app’s launch faster and process events quicker. Using a networking example, rather than performing a synchronous network call on the main thread, move it to an asynchronous background queue. By moving this work to a background queue, the main thread can process scroll events as they happen, allowing the app to be more responsive.

![A timing diagram with two threads, the main thread and a dispatch queue thread. The main thread uses the dispatch queue as an asynchronous thread for networking, allowing the main thread to handle scroll events while the network request is in progress. After the networking is complete, the resulting UI update is done on the main thread.](https://docs-assets.developer.apple.com/published/7a42f532e1752e43dece9417341fddc8/addressing-watchdog-terminations-2%402x.png)

If the long-running code is from one of the system frameworks, determine whether the framework provides an alternate approach that moves the work off the main thread. For example, consider loading a complex 3D model in [`RealityKit`](https://developer.apple.com/documentation/RealityKit) using [`loadAsync(contentsOf:withName:)`](https://developer.apple.com/documentation/RealityKit/Entity/loadAsync(contentsOf:withName:)) instead of [`load(contentsOf:withName:)`](https://developer.apple.com/documentation/RealityKit/Entity/load(contentsOf:withName:)), which is synchronous. As a different example, [`Vision`](https://developer.apple.com/documentation/Vision) provides  [`preferBackgroundProcessing`](https://developer.apple.com/documentation/Vision/VNRequest/preferBackgroundProcessing), which is a hint that the system should move processing of analysis requests off the main thread.

If networking code is contributing to your watchdog termination, consider these common solutions:

- Run your networking code asynchronously using [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession). This is the best solution. Asynchronous networking code has many advantages, including accessing the network safely without having to worry about threads.
- Instead of using [`SCNetworkReachability`](https://developer.apple.com/documentation/SystemConfiguration/scnetworkreachability-g7d), use [`NWPathMonitor`](https://developer.apple.com/documentation/Network/NWPathMonitor) to receive updates when the network path changes. The system delivers updates on a queue that you pass in when calling [`start(queue:)`](https://developer.apple.com/documentation/Network/NWPathMonitor/start(queue:)), so path updates function safely off the main thread.
- Perform synchronous networking on a secondary thread. If it’s prohibitively difficult to run your networking code asynchronously, such as when using a large portable code base that assumes synchronous networking, avoid the watchdog by running the synchronous networking code on a secondary thread.
- Resolving DNS manually isn’t recommended for most situations. Use [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) to have the system handle DNS resolution on your behalf. If it’s prohibitively difficult to switch and you continue to need to DNS addresses manually, use an asynchronous API like `CFHost` or the APIs in `<dns_sd.h>`.

## See Also

- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/addressing-watchdog-terminations)*