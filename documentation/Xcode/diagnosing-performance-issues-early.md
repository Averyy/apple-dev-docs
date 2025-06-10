# Diagnosing performance issues early

**Framework**: Xcode

Diagnose potential performance issues in your app during testing with the Thread Performance Checker tool in Xcode.

#### Overview

Identifying potential performance issues during development saves testing time later. Resolving performance issues, such as priority inversions and non-UI work on the main thread, makes your app responsive. Priority inversions occur when a low-priority thread blocks a higher-priority thread, which can lead to an unresponsive app. Similarly, non-UI work, such as synchronous networking or I/O on the main thread, can block the main thread for hundreds of milliseconds, which prevents people from interacting with your app.

The Thread Performance Checker tool detects priority inversions and non-UI work on the main thread. It doesn’t require any recompilation. Use the Thread Performance Checker tool to detect, diagnose, and resolve performance issues.

##### Understand the Detected Issues

The Thread Performance Checker tool surfaces issues in the Issue navigator and the source editor. Read the diagnostic message carefully.

![A screenshot of a Priority Inversion issue text in the source editor.](https://docs-assets.developer.apple.com/published/cebd1e73a23e69cd03ffee45e99e962f/diagnosing-performance-issues-early-1%402x.png)

To understand the issue in depth, expand the backtrace of the issue in the Issue navigator.

![A screenshot of the expanded backdtrace in the Issue navigator.](https://docs-assets.developer.apple.com/published/c26fbff407d8e560d6d2c51d61a62e11/diagnosing-performance-issues-early-2%402x.png)

The issues surfaced point to code in your project that can cause hangs. Hangs occur when your app is unresponsive for hundreds of milliseconds. To learn more about hangs, see [`Improving app responsiveness`](improving-app-responsiveness.md) and the WWDC session video [`Understand and eliminate hangs from your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10258/).

##### Diagnose and Resolve Priority Inversions

If you use concurrency primitives, such as [`dispatch_semaphore_wait`](https://developer.apple.com/documentation/dispatch/1453087-dispatch_semaphore_wait) and [`dispatch_group_wait`](https://developer.apple.com/documentation/dispatch/1452794-dispatch_group_wait), in your code or invoke APIs that use them, your app is susceptible to priority inversions if there is a mismatch in the quality-of-service (QoS) class of the dispatch queues your app uses. When you use these primitives, the system can’t automatically propagate priority from the higher-priority thread to the lower-priority thread. You can take these precautions to avoid priority inversions in your code:

- Don’t use `dispatch_semaphore_wait` and `dispatch_group_wait` to emulate synchronous behavior when calling an asynchronous internal method or API. Remove the code if the underlying functionality is unnecessary.
- Ensure that the QoS of the waiting thread is the same as or lower than the QoS of the signaling thread when a synchronous variant isn’t available. Explicitly classify the QoS of the work when you create a [`Dispatch Queue`](https://developer.apple.com/documentation/Dispatch/dispatch-queue) or an [`OperationQueue`](https://developer.apple.com/documentation/Foundation/OperationQueue).

The code in `initiateBackgroundWork` below explicitly creates a dispatch queue with background QoS. `doBackgroundWorkAsync` signals the completion of the background work it does asynchronously at background QoS. After the background work completes, it updates the UI label on the main thread at [`userInteractive`](https://developer.apple.com/documentation/Dispatch/DispatchQoS/userInteractive) QoS.

```swift
func initiateBackgroundWork() {
    let dispatchSemaphore = DispatchSemaphore(value: 0)
    let backgroundQueue = DispatchQueue(label: "background_queue", 
                                        qos: .background)
    
    backgroundQueue.async {
        // Perform work on a separate thread using the quality-of-service level 
        // for background maintenance or cleanup tasks and signal when the work completes.
       doBackgroundWorkAsync {
           dispatchSemaphore.signal()
       }
       
       _ = dispatchSemaphore.wait(timeout: DispatchTime.distantFuture)
       
       DispatchQueue.main.async { [weak self] in
           self?.label.text = "Background work completed"
       }
    })
}
```

To learn more about priority inversions and QoS, see [`Modernizing Grand Central Dispatch Usage`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2017/706/) and [`Energy Efficiency Guide for iOS Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html).

##### Diagnose and Eliminate Non Ui Work on the Main Thread

Long-running synchronous I/O and networking on the main thread can make your app unresponsive. For example, to perform real-time capture, you instantiate an [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) object and add appropriate inputs and outputs. Invoking the [`startRunning()`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/startRunning()) method of an `AVCaptureSession` object on the main thread of your app can lead to hangs. You can take these precautions to avoid non-UI work on the main thread:

- Don’t synchronously read from or write to files and I/O devices on the main thread. Instead, do the work on a separate serial dispatch queue, and notify the completion of I/O by enqueuing a block onto the main queue.
- Use the asynchronous variant of an API that performs I/O to do that work off the main thread.
- Don’t perform synchronous networking on the main thread of your app. Instead, use an asynchronous networking API, such as [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession).

##### Disable the Thread Performance Checker Tool

The Thread Performance Checker tool is enabled by default for schemes that build an app in your project. To disable it, choose Product > Scheme > Edit Scheme to display the scheme editor. Select the Run schemes, navigate to the Diagnostics section, and unselect the Thread Performance Checker tool checkbox.

![A screenshot of the Scheme Editor with the Thread Performance Checker checkbox selected.](https://docs-assets.developer.apple.com/published/982a500a5193deb7fde595751b084213/diagnosing-performance-issues-early-3%402x.png)

In addition to the Thread Performance Checker tool, always test your code using a comprehensive set of performance tests. For more information about testing your code, see [`Testing`](testing.md).

> ❗ **Important**: The Thread Performance Checker tool is currently supported only on macOS and iOS.

Resolution of certain performance issues may require significant code refactoring or redesign of the underlying logic. To suppress the warning for issues you intend to address at a later time, set the `PERFC_SUPPRESSION_FILE` environment variable to provide a list of classes and methods in a suppression file. The Thread Performance Checker tool only shows issues that don’t involve those classes and methods. Use the following format for your suppression file:

```other
class:UIActivityViewController
class:NSThread
method:-[UIViewController view]
method:readv
```

## See Also

- [Addressing watchdog terminations](addressing-watchdog-terminations.md)
  Identify the signature of an unresponsive app terminated by the watchdog, and address the issue.
- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Analyzing responsiveness issues in your shipping app](analyzing-responsiveness-issues-in-your-shipping-app.md)
  Identify responsiveness issues your users encounter, and use the hang and hitch data in Xcode Organizer to determine which issues are most important to fix.
- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Understanding user interface responsiveness](understanding-user-interface-responsiveness.md)
  Make your app more responsive by examining the event-handling and rendering loop.
- [Understanding and improving SwiftUI performance](understanding-and-improving-swiftui-performance.md)
  Identify and address long-running view updates, and reduce the frequency of updates.
- [Understanding hangs in your app](understanding-hangs-in-your-app.md)
  Determine the cause for delays in user interactions by examining the main thread and the main run loop.
- [Understanding hitches in your app](understanding-hitches-in-your-app.md)
  Determine the cause of interruptions in motion by examining the render loop.
- [Reducing your app’s launch time](reducing-your-app-s-launch-time.md)
  Create a more responsive experience with your app by minimizing time spent in startup.
- [Reducing terminations in your app](reduce-terminations-in-your-app.md)
  Minimize how frequently the system stops your app by addressing common termination reasons.
- [Reducing disk writes](reducing-disk-writes.md)
  Improve your app’s responsiveness by optimizing how it writes data to permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/diagnosing-performance-issues-early)*