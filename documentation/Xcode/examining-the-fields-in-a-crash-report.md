# Examining the fields in a crash report

**Framework**: Xcode

Understand the structure of a crash report and the information each field contains.

#### Overview

Each section of a crash report contains information to help you diagnose the source of a crash.

![An outline of a crash report showing where each section is located.](https://docs-assets.developer.apple.com/published/cb64dd660c25af51a6a38152f138872e/examining-the-fields-in-a-crash-report-1%402x.png)

##### Header

A crash report begins with a header section that describes the environment the crash occurred in.

```other
Incident Identifier: 6156848E-344E-4D9E-84E0-87AFD0D0AE7B
CrashReporter Key:   76f2fb60060d6a7f814973377cbdc866fffd521f
Hardware Model:      iPhone8,1
Process:             TouchCanvas [1052]
Path:                /private/var/containers/Bundle/Application/51346174-37EF-4F60-B72D-8DE5F01035F5/TouchCanvas.app/TouchCanvas
Identifier:          com.example.apple-samplecode.TouchCanvas
Version:             1 (3.0)
Code Type:           ARM-64 (Native)
Role:                Foreground
Parent Process:      launchd [1]
Coalition:           com.example.apple-samplecode.TouchCanvas [1806]

Date/Time:           2020-03-27 18:06:51.4969 -0700
Launch Time:         2020-03-27 18:06:31.7593 -0700
OS Version:          iPhone OS 13.3.1 (17D50)
```

The fields in the header can contain the following information. No single crash report contains all of these fields.

- `Incident Identifier`: A unique identifier for the report. Two reports never share the same `Incident Identifier`.
- `CrashReporter Key`: An anonymized per-device identifier. Two reports from the same device contain identical values. This identifier is reset upon erasing the device.
- `Beta Identifier`: A unique identifier for the combination of the device and vendor of the crashed application. Two reports for apps from the same vendor and from the same device contain identical values. This field is only present for TestFlight builds of an app, and replaces the `CrashReporter Key` field.
- `Hardware Model`: The specific device model the app was running on.
- `Process`: The executable name for the process that crashed. This matches the [`CFBundleExecutable`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleExecutable) value in the app’s information property list. The number in brackets is the process ID.
- `Path`: The location of the executable on disk. macOS replaces user-identifable path components with placeholder values to protect privacy.
- `Identifier`: The [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier) of the process that crashed. If the binary doesn’t have a [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier), this field contains either the process name or a placeholder value.
- `Version`: The version of the process that crashed. The value is a concatenation of the app’s [`CFBundleVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleVersion) and [`CFBundleShortVersionString`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleShortVersionString).
- `AppStoreTools`: The version of Xcode used to compile your app’s bitcode and to thin your app to device specific variants.
- `AppVariant`: The specific variant of your app produced by app thinning. This field contains multiple values, described later in this section.
- `Code Type`: The CPU architecture of the process that crashed. The value is one of `ARM-64`, `ARM`, `X86-64`, or `X86`.
- `Role`: The [`task_role`](https://developer.apple.comhttps://opensource.apple.com/source/xnu/xnu-3248.60.10/osfmk/mach/task_policy.h) assigned to the process at the time of termination. This field is generally not helpful when you analyze a crash report.
- `Parent Process`: The name and process ID (in square brackets) of the process that launched the crashed process.
- `Coalition`: The name of the process coalition containing the app. Process coalitions track resource usage among groups of related processes, such as an operating system process supporting a specific API’s functionality in an app. Most processes, including app extensions, form their own coalition.
- `Date/Time`: The date and time of the crash.
- `Launch Time`: The date and time the app launched.
- `OS Version`: The operating system version, including the build number, on which the crash occurred.

The `AppVariant` field contains three values separated by colons, for example, `1:iPhone10,6:12.2`. These fields represent:

- An internal system value. This value isn’t useful for diagnosing a crash. In the example, this value is `1`.
- The name of the thinning variant. The variant represents a class of devices with similar characteristics, such as screen scale, memory class, and Metal GPU family. The thinning variant’s name doesn’t indicate the exact hardware model the crash report is from, and may differ from the `Hardware Model` field. In the example, this value is `iPhone10,6`.
- The operating system version variant. For each class of devices, app thinning creates additional variants for different versions of the operating system. In the example, this value is `12.2`, indicating this variant targets iOS devices running iOS 12.2 or higher.

##### Exception Information

Every crash report contains exception information. This information section tells you how the process terminated, but it may not fully explain why the app terminated. This information is important, but is often overlooked.

```other
Exception Type:  EXC_BREAKPOINT (SIGTRAP)
Exception Codes: 0x0000000000000001, 0x0000000102afb3d0
```

> **Note**: This exception information doesn’t refer to language exceptions thrown by an API or language features in Objective-C or C++. Crash reports record language exception information separately.

The following fields provide information about the exception. No single crash report contains all of these fields.

- `Exception Type`: The name of the Mach exception that terminated the process, along with the name of the corresponding BSD termination signal in parentheses. See [`Understanding the exception types in a crash report`](understanding-the-exception-types-in-a-crash-report.md).
- `Exception Codes`: Processor specific information about the exception encoded into one or more 64-bit hexadecimal numbers. Typically, this field isn’t present because the operating system presents the information as human-readable information in the other fields of this section.
- `Exception Subtype`: The human-readable description of the exception codes.
- `Exception Message`: Additional human-readable information extracted from the exception codes.
- `Exception Note`: Additional information that isn’t specific to one exception type. If this field contains `EXC_CORPSE_NOTIFY`, the crash didn’t originate from a hardware trap, either because the process was explicitly terminated by the operating system or the process called `abort()`. If this field contains `SIMULATED (this is NOT a crash)`, the process didn’t crash, but the operating system might have subsequently requested termination of the process. If this field contains `NON-FATAL CONDITION (this is NOT a crash)`, the process didn’t terminate, because the issue that created the crash report wasn’t fatal.
- `Termination Reason`: Exit reason information specified when the operating system terminates a process. Key operating system components, both inside and outside of a process, terminate the process upon encountering a fatal error and record the reason in this field. Examples of the information you can find in this field are messages about an invalid code signature, a missing dependent library, or accessing privacy sensitive information without a purpose string.
- `Triggered by Thread` or `Crashed Thread`: The thread on which the exception originated.

##### Diagnostic Messages

The operating system sometimes includes additional diagnostic information. This information uses a variety of formats, depending on reason for the crash, and isn’t present in every crash report.

Framework error messages occurring just before the process terminated appear in the `Application Specific Information` field. In this example, the [`Dispatch`](https://developer.apple.com/documentation/Dispatch) framework logged an error about incorrect use of a dispatch queue:

```other
Application Specific Information:
BUG IN CLIENT OF LIBDISPATCH: dispatch_sync called on queue already owned by current thread
```

> **Note**: `Application Specific Information` is sometimes elided from a crash report to avoid logging privacy-sensitive information in the message.

Terminations due to a watchdog violation contain a `Termination Description` field with information about why the watchdog triggered.

```other
Termination Description: SPRINGBOARD, 
    scene-create watchdog transgression: application<com.example.MyCoolApp>:667
    exhausted real (wall clock) time allowance of 19.97 seconds 
```

[`Addressing watchdog terminations`](addressing-watchdog-terminations.md) goes into more detail about watchdog terminations and how to interpret this information.

Terminations due to a memory access issue contain information about the virtual memory regions in the `VM Region Info` field.

```other
VM Region Info: 0 is not in any region.  Bytes before following region: 4307009536
      REGION TYPE                      START - END             [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
--->  
      __TEXT                 0000000100b7c000-0000000100b84000 [   32K] r-x/r-x SM=COW  ...pp/MyGreatApp
```

[`Investigating memory access crashes`](investigating-memory-access-crashes.md) goes into more detail about this information.

##### Backtraces

Each thread of the crashed proces is captured as a backtrace, documenting the code running on the thread when the process terminated. The backtraces are similar to what you see when you pause the process with the debugger. Crashes caused by a language exception include an additional backtrace, the `Last Exception Backtrace`, located before the first thread. If your crash report contains a `Last Exception Backtrace`, see [`Addressing language exception crashes`](addressing-language-exception-crashes.md) for information specific to language exception crashes.

The first line of each backtrace lists the thread number and the thread name. For privacy reasons, crash reports delivered through the [`Crashes Organizer`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev675635e70) in Xcode don’t contain thread names. This example shows the backtraces for three threads; `Thread 0` crashed, and is identified as the app’s main thread by its name:

```other
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   TouchCanvas                       0x0000000102afb3d0 CanvasView.updateEstimatedPropertiesForTouches(_:) + 62416 (CanvasView.swift:231)
1   TouchCanvas                       0x0000000102afb3d0 CanvasView.updateEstimatedPropertiesForTouches(_:) + 62416 (CanvasView.swift:231)
2   TouchCanvas                       0x0000000102af7d10 ViewController.touchesMoved(_:with:) + 48400 (<compiler-generated>:0)
3   TouchCanvas                       0x0000000102af80b8 @objc ViewController.touchesMoved(_:with:) + 49336 (<compiler-generated>:0)
4   UIKitCore                         0x00000001ba9d8da4 forwardTouchMethod + 328
5   UIKitCore                         0x00000001ba9d8e40 -[UIResponder touchesMoved:withEvent:] + 60
6   UIKitCore                         0x00000001ba9d8da4 forwardTouchMethod + 328
7   UIKitCore                         0x00000001ba9d8e40 -[UIResponder touchesMoved:withEvent:] + 60
8   UIKitCore                         0x00000001ba9e6ea4 -[UIWindow _sendTouchesForEvent:] + 1896
9   UIKitCore                         0x00000001ba9e8390 -[UIWindow sendEvent:] + 3352
10  UIKitCore                         0x00000001ba9c4a9c -[UIApplication sendEvent:] + 344
11  UIKitCore                         0x00000001baa3cc20 __dispatchPreprocessedEventFromEventQueue + 5880
12  UIKitCore                         0x00000001baa3f17c __handleEventQueueInternal + 4924
13  UIKitCore                         0x00000001baa37ff0 __handleHIDEventFetcherDrain + 108
14  CoreFoundation                    0x00000001b68a4a00 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 24
15  CoreFoundation                    0x00000001b68a4958 __CFRunLoopDoSource0 + 80
16  CoreFoundation                    0x00000001b68a40f0 __CFRunLoopDoSources0 + 180
17  CoreFoundation                    0x00000001b689f23c __CFRunLoopRun + 1080
18  CoreFoundation                    0x00000001b689eadc CFRunLoopRunSpecific + 464
19  GraphicsServices                  0x00000001c083f328 GSEventRunModal + 104
20  UIKitCore                         0x00000001ba9ac63c UIApplicationMain + 1936
21  TouchCanvas                       0x0000000102af16dc main + 22236 (AppDelegate.swift:12)
22  libdyld.dylib                     0x00000001b6728360 start + 4

Thread 1:
0   libsystem_pthread.dylib           0x00000001b6645758 start_wqthread + 0

Thread 2:
0   libsystem_pthread.dylib           0x00000001b6645758 start_wqthread + 0
...
```

After the thread number, each line of a backtrace represents a stack frame in the backtrace.

```other
0   TouchCanvas                       0x0000000102afb3d0 CanvasView.updateEstimatedPropertiesForTouches(_:) + 62416 (CanvasView.swift:231)
```

Each column of the stack frame contains information about the code executing at the time of the crash. The following list uses the components of stack frame 0 from the example above.

- `0`. The stack frame number. Stack frames are in calling order, where frame 0 is the function that was executing at the time execution halted. Frame 1 is the function that called the function in frame 0, and so on.
- `TouchCanvas`. The name of the binary containing the function that is executing.
- `0x0000000102afb3d0`. The address of the machine instruction that is executing. For frame 0 in each backtrace, this is the address of the machine instruction executing on a thread when the process terminated. For other stack frames, this is the address of first machine instruction that executes after control returns to that stack frame.
- `CanvasView.updateEstimatedPropertiesForTouches(_:)`. In a fully symbolicated crash report, the name of the function that is executing. For privacy reasons, the function name is sometimes limited to the first 100 characters.
- `62416`. The number after the `+` is the byte offset from the function’s entry point to the current instruction in the function.
- `CanvasView.swift:231`. The file name and line number containing the code, if you have a `dSYM` file for the binary.

In some situations, the file name or the line number information won’t correspond to the orginial source code:

- If the source file name is `<compiler-generated>`, the compiler created the code for that frame, and the code isn’t in your source files. If this is top frame in the crashed thread, look at the preceeding few stack frames for clues.
- If the line number for a source file is `0`, this means the backtrace doesn’t map to a specific line of code in the original code. This is because the compiler optimized the code, such as by inlining functions, and the code executing at the time of the crash doesn’t correspond to an exact line in the orignial code. The function name for the frame is still a clue in this situation.

##### Thread State

The thread state section of a crash report lists the CPU registers and their values for the crashed thread when the app terminated. Understanding the thread state is an advanced topic that requires understanding of the application binary interface (ABI). See [`Writing ARM64 code for Apple platforms`](writing-arm64-code-for-apple-platforms.md).

```other
Thread 0 crashed with ARM Thread State (64-bit):
    x0: 0x0000000000000001   x1: 0x0000000000000000   x2: 0x0000000000000000   x3: 0x000000000000000f
    x4: 0x00000000000001c2   x5: 0x000000010327f6c0   x6: 0x000000010327f724   x7: 0x0000000000000120
    x8: 0x0000000000000001   x9: 0x0000000000000001  x10: 0x0000000000000001  x11: 0x0000000000000000
   x12: 0x00000001038612b0  x13: 0x000005a102b075a7  x14: 0x0000000000000100  x15: 0x0000010000000000
   x16: 0x00000001c3e6c630  x17: 0x00000001bae4bbf8  x18: 0x0000000000000000  x19: 0x0000000282c14280
   x20: 0x00000001fe64a3e0  x21: 0x4000000281f1df10  x22: 0x0000000000000001  x23: 0x0000000000000000
   x24: 0x0000000000000000  x25: 0x0000000282c14280  x26: 0x0000000103203140  x27: 0x00000001bacf4b7c
   x28: 0x00000001fe5ded08   fp: 0x000000016d311310   lr: 0x0000000102afb3d0
    sp: 0x000000016d311200   pc: 0x0000000102afb3d0 cpsr: 0x60000000
   esr: 0xf2000001  Address size fault
```

Registers provide extra information for crashes caused by memory access issues. [`Understand the crashed thread’s registers`](analyzing-a-crash-report#Understand-the-crashed-threads-registers.md) discusses that scenario further.

##### Binary Images

The binary images section of a crash report lists all code loaded in the process at the time of termination, such as the app executable and system frameworks. Each line in the Binary Images section represents a single binary image. iOS, iPadOS, tvOS, visionOS, and watchOS use the following format:

```other
Binary Images:
0x102aec000 - 0x102b03fff TouchCanvas arm64  <fe7745ae12db30fa886c8baa1980437a> /var/containers/Bundle/Application/51346174-37EF-4F60-B72D-8DE5F01035F5/TouchCanvas.app/TouchCanvas
...
```

This list contains the components from the preceding example:

- `0x102aec000 - 0x102b03fff`. The binary image’s address range within the process. The first address is the binary’s load address. See [`Symbolicate the crash report with the command line`](adding-identifiable-symbol-names-to-a-crash-report#Symbolicate-the-crash-report-with-the-command-line.md) for how to use this value.
- `TouchCanvas`. The binary name.
- `arm64`. The CPU architecture from the binary image that the operating system loaded into the process.
- `fe7745ae12db30fa886c8baa1980437a`. A build UUID that uniquely identifies the binary image. Use this value to locate the corresponding `dSYM` file when symbolicating the crash report. See [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md) for more information on build UUIDs.
- `/var/containers/.../TouchCanvas.app/TouchCanvas`. The path to the binary on disk. macOS replaces user-identifable path components with placeholder values to protect privacy.

macOS uses the following format for this section:

```other
Binary Images:
       0x1025e5000 -        0x1025e6ffb +com.example.apple-samplecode.TouchCanvas (1.0 - 1) <5ED9BD63-2A55-3DDD-B3FF-EFCF61382F6F> /Users/USER/*/TouchCanvas.app/Contents/MacOS/TouchCanvas
```

This list contains the components from the preceding example:

- `0x105f97000 - 0x105f98ffb`. The binary image’s address range within the process. The first address is the binary’s load address. See [`Symbolicate the crash report with the command line`](adding-identifiable-symbol-names-to-a-crash-report#Symbolicate-the-crash-report-with-the-command-line.md) for how to use this value.
- `+com.example.apple-samplecode.TouchCanvas`. The [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier) of the binary. The `+` prefix indicates the binary is not part of macOS.
- `1.0 - 1`. The binary’s [`CFBundleShortVersionString`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleShortVersionString) and [`CFBundleVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleVersion).
- `5ED9BD63-2A55-3DDD-B3FF-EFCF61382F6F`. A build UUID that uniquely identifies the binary image. Use this value to locate the corresponding `dSYM` file when symbolicating the crash report. See [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md) for more information on build UUIDs.
- `/Users/USER/*/TouchCanvas.app/Contents/MacOS/TouchCanvas`. The path to the binary on disk. macOS replaces user-identifable path components with placeholder values to protect privacy.

## See Also

- [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md)
  Replace hexadecimal addresses in a crash report with function names and line numbers that correspond to your app’s code.
- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)
  Find patterns in crash reports that identify common problems, and investigate the issue based on the pattern.
- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.
- [Interpreting the JSON format of a crash report](interpreting-the-json-format-of-a-crash-report.md)
  Understand the structure and properties of the objects the system includes in the JSON of a crash report.
- [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)
  Learn what the exception type tells you about why your app crashed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/examining-the-fields-in-a-crash-report)*