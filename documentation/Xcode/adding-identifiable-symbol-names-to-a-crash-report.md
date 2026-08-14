# Adding identifiable symbol names to a crash report

**Framework**: Xcode

Replace hexadecimal addresses in a crash report with function names and line numbers that correspond to your app’s code.

#### Overview

When an app crashes, the operating system collects diagnostic information about what the app was doing at the time of the crash. One of the most important parts of the crash report is the thread backtraces, which appear as hexadecimal addresses. You translate these addresses into readable function names and line numbers — a process called *symbolication* — to understand why your app crashed. To learn about the structure of a backtrace, see [`Backtraces`](examining-the-fields-in-a-crash-report#Backtraces.md).

If you include debug symbols when you upload your app to App Store Connect for distribution in the App Store or TestFlight, the Crashes organizer in Xcode automatically symbolicates the crash reports for you. For more information, see [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md).

##### Determine Whether a Crash Report Is Symbolicated

A crash report can be fully symbolicated, partially symbolicated, or unsymbolicated. To diagnose an app issue, you need at least a partially symbolicated crash report — an unsymbolicated crash report is rarely useful.

A fully symbolicated crash report displays function names instead of hexadecimal addresses on every frame of the backtrace. Each frame represents a single function call that was on the call stack when your app crashed. Together, the frames show the functions from your app and the operating system frameworks that were active at that moment. Fully symbolicated crash reports give you the most insight into the crash, like in the following example:

```shell
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   TouchCanvas                              0x1046a59b4 Line.updateRectForExistingPoint(_:) + 988
1   TouchCanvas                              0x1046a56d0 Line.updateRectForExistingPoint(_:) + 248
2   TouchCanvas                              0x1046ab130 CanvasView.updateEstimatedPropertiesForTouches(_:) + 832
3   TouchCanvas                              0x1046a8610 @objc ViewController.touchesEstimatedPropertiesUpdated(_:) + 120
4   UIKitCore                                0x1a6cff6ec forwardMethod1 + 108
5   UIKitCore                                0x1a6cff6ec forwardMethod1 + 108
6   UIKitCore                                0x1a73033fc -[_UIEstimatedTouchRecord _dispatchWithCurrentUpdates] + 340
7   UIKitCore                                0x1a6ba5c40 -[UIEventEnvironment _dispatchAndRemoveStaleEstimationUpdateRecordsWithEventTime:upToRecord:] + 268
8   UIKitCore                                0x1a5932074 __processEventQueue + 5400
9   UIKitCore                                0x1a5924c50 updateCycleEntry + 172
10  UIKitCore                                0x1a5932ee4 _UIUpdateSequenceRunNext + 128
11  UIKitCore                                0x1a5932374 schedulerStepScheduledMainSectionContinue + 60  
    
```

A partially symbolicated crash report displays function names for some frames of the backtrace and only hexadecimal addresses for others. Depending on the type of crash and which frames include symbol information, the report may give you enough information to understand the crash, as the following example demonstrates:

```shell
Thread 0 name:   Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   TouchCanvas                              0x1045a19b4 0x10459c000 + 22964
1   TouchCanvas                              0x1045a16d0 0x10459c000 + 22224
2   TouchCanvas                              0x1045a7130 0x10459c000 + 45360
3   TouchCanvas                              0x1045a4610 0x10459c000 + 34320
4   UIKitCore                                0x1a6cff6ec forwardMethod1 + 108
5   UIKitCore                                0x1a6cff6ec forwardMethod1 + 108
6   UIKitCore                                0x1a73033fc -[_UIEstimatedTouchRecord _dispatchWithCurrentUpdates] + 340
7   UIKitCore                                0x1a6ba5c40 -[UIEventEnvironment _dispatchAndRemoveStaleEstimationUpdateRecordsWithEventTime:upToRecord:] + 268
8   UIKitCore                                0x1a5932074 __processEventQueue + 5400
9   UIKitCore                                0x1a5924c50 updateCycleEntry + 172
10  UIKitCore                                0x1a5932ee4 _UIUpdateSequenceRunNext + 128
11  UIKitCore                                0x1a5932374 schedulerStepScheduledMainSectionContinue + 60
    
```

An unsymbolicated crash report displays only hexadecimal addresses in the backtraces, with no function names, as shown in the following example:

```shell
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   libswiftCore.dylib                0x00000001bd38da70 0x1bd149000 + 2378352
1   libswiftCore.dylib                0x00000001bd38da70 0x1bd149000 + 2378352
2   libswiftCore.dylib                0x00000001bd15958c 0x1bd149000 + 66956
3   libswiftCore.dylib                0x00000001bd15c814 0x1bd149000 + 79892
4   TouchCanvas                       0x00000001022cbfa8 0x1022c0000 + 49064
5   TouchCanvas                       0x00000001022c90b0 0x1022c0000 + 37040
6   TouchCanvas                       0x00000001022e7374 0x1022c0000 + 160628
7   TouchCanvas                       0x00000001022df754 0x1022c0000 + 128852
8   TouchCanvas                       0x00000001022df7e8 0x1022c0000 + 129000
9   UIKitCore                         0x00000001b3da6230 0x1b3348000 + 10871344
10  UIKitCore                         0x00000001b3da6230 0x1b3348000 + 10871344
11  UIKitCore                         0x00000001b3e01e24 0x1b3348000 + 11247140
    
```

##### Symbolicate the Crash Report in Xcode

To symbolicate a crash report from your device, connect the device to your Mac, click the Reports tab in the Device Hub app, then choose Crashes from the Inspector menu. In the list that appears, select the crash report. For more information, see [`Device Hub`](device-hub.md) and [`Managing your simulated and physical devices in Device Hub`](managing-your-simulated-and-physical-devices-in-device-hub.md).

> ❗ **Important**: Crash reports must have the `.crash` or `.ips` file extension. If the file has a different extension or no extension, rename the file before symbolicating.

If you receive a crash report from an external source, open the file in Xcode. Choose the applicable project when Xcode prompts you. ![An Xcode dialog to choose a project for symbolication. The dialog shows Open and Cancel buttons.](/images/com.apple.Xcode/adding-identifiable-symbol-names-to-a-crash-report-01@2x.png)

After you choose Open, Xcode attempts to symbolicate all addresses in every thread’s backtrace.

If symbolication is incomplete, try the following:

- If Xcode fails to symbolicate the operating system’s frameworks, download the device symbols for the operating system version in the crash report. For more information, see [`Acquiring operating system symbol information`](acquiring-operating-system-symbol-information.md).
- If Xcode fails to symbolicate an address for your app, app extension, or frameworks, use Spotlight to find the required `.dSYM` files. For more information, see [`Locating a missing debug symbol file`](locating-a-missing-debug-symbol-file.md).
- If your app uses third-party frameworks or packages, contact their developers to obtain the `.dSYM` file.

##### Symbolicate the Crash Report Using a Command Line Tool

You can symbolicate your crash report in Terminal using the `crashlog` command. Enter `xcrun crashlog` with the path to the crash report you want to symbolicate, as shown here:

```shell
% xcrun crashlog <path-to-crashReport>
```

The `xcrun crashlog` command is a shortcut to invoke a Python module that supports parsing and symbolicating crash reports. The module installs `crashlog` into the LLDB command interpreter. After resolving the symbols in each binary image that a crash report references, `crashlog` provides function names, source file names, and line numbers for every frame of the backtrace, like in the following example:

```shell
% xcrun crashlog /Users/.../TouchCanvas.ips
(lldb) command script import lldb.macosx
"crashlog" and "save_crashlog" commands have been installed, use the "--help" options on these commands
...
(lldb) crashlog /Users/.../TouchCanvas.ips
Getting symbols for E3EA8743-C9E6-3C68-BF04-8D51363B689D /var/containers/.../TouchCanvas.app/TouchCanvas...
...
Resolved symbols for E3EA8743-C9E6-3C68-BF04-8D51363B689D /Users/.../TouchCanvas.app/TouchCanvas...
(lldb) process status --verbose
warning: TouchCanvas was compiled with optimization - stepping may behave oddly; variables may not be available.
Process 767 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = Swift runtime failure: Index out of range
    frame #0: 0x00000001045a19b4 TouchCanvas`Swift runtime failure: Index out of range at Line.swift:0:27 [synthetic] [opt] [inlined]
note: This address is not associated with a specific line of code. This may be due to compiler optimizations.
(lldb) thread backtrace --extended true
Couldn't find the Objective-C runtime library in loaded images.
...
* thread #1, queue = 'com.apple.main-thread', stop reason = Swift runtime failure: Index out of range                                                 
  * frame #0: 0x00000001045a19b4 TouchCanvas`Swift runtime failure: Index out of range at Line.swift:0:27 [synthetic] [opt] [inlined]
    frame #1: 0x00000001045a16cf TouchCanvas`Line.updateRectForExistingPoint(point=<unavailable>) at <compiler-generated>:0 [synthetic] [opt]
    frame #2: 0x00000001045a712f TouchCanvas`Line.updateWithTouch(touch=<unavailable>) at Line.swift:29:24 [synthetic] [opt]
    frame #3: 0x00000001045a460f TouchCanvas`ViewController.touchesEstimatedPropertiesUpdated(touches=<unavailable>) at ViewController.swift:121:20 [synthetic] [opt] [inlined]
...
```

Alternatively, if you already have an active LLDB session, you can import `lldb.macosx.crashlog`, then run `crashlog` with the path to the crash report you want to symbolicate, like this:

```shell
(lldb) command script import lldb.macosx.crashlog
(lldb) crashlog /Users/.../TouchCanvas.ips
```

The `crashlog` command provides additional options you can use to adjust its output. For example, you can parse and load your crash report in a scripted process, choose which frames and how many lines `crashlog` disassembles, and configure the command to display the image list. To learn about these options, enter `xcrun crashlog --help` in Terminal.

##### Symbolicate the Crash Report Using a Python Script

The `CrashSymbolicator.py` Python 3 script supports JSON-format crash reports and inlined frames when run with its default options. Find it in the `Contents/SharedFrameworks/CoreSymbolicationDT.framework/Resources` directory within the Xcode app bundle. In Terminal, navigate to this directory in your Xcode installation as follows:

```shell
% xcode-select -p
/Applications/Xcode.app/Contents/Developer

% cd /Applications/Xcode.app/Contents/SharedFrameworks/CoreSymbolicationDT.framework/Resources
```

Enter `python3 CrashSymbolicator.py` with the path to your crash report and all the `.dSYM` files that the binary requires for symbolication, like this:

```shell
% python3 CrashSymbolicator.py <path-to-crashReport> -d <path-to-dSYM>
```

This command prints the result to `stdout`, like in the following example:

```shell
% python3 CrashSymbolicator.py /Users/.../TouchCanvas.ips -d /Users/.../TouchCanvas.app.dSYM
Symbolicating thread 113506
Symbolicating thread 113533
...
{"app_name":"TouchCanvas" ...}
...
"frames": [
{
"imageOffset": 22964,
"imageIndex": 0,
"symbol": "Swift runtime failure: Index out of range",
"sourceFile": "Line.swift",
"sourceLine": 0,
"symbolLocation": 0,
"inline": "true"
},
...
{
"imageOffset": 22964,
"imageIndex": 0,
"symbol": "Line.updateRectForExistingPoint(_:)",
"sourceFile": "Line.swift",
"sourceLine": 230,
"symbolLocation": 988
},
...
```

To save the command’s output to a file, add the `-o` option:

```shell
% python3 CrashSymbolicator.py /Users/.../TouchCanvas.ips -d /Users/.../TouchCanvas.app.dSYM -o /Users/.../SymbolicatedTouchCanvas.ips

```

To learn about all the options the script offers, enter `python3 CrashSymbolicator.py --help` in Terminal.

##### Symbolicate Individual Addresses of the Crash Report

For specialized debugging situations, such as symbolicating individual stack frames at the LLDB command line, use the `atos` command. This command converts hexadecimal addresses to function names and line numbers in your source code.

To symbolicate a hexadecimal address in your crash report using `atos`, inspect the stack frame that contains it. Note the binary image name in the second column. For example, the following backtrace highlights a frame at line 3 with `0x1045a4610` as the address to symbolicate and a binary image named `TouchCanvas`:

![A crash report with line 3 highlighted. The line shows a hexadecimal address.](/images/com.apple.Xcode/adding-identifiable-symbol-names-to-a-crash-report-02@2x.png)

> **Note**: If the symbol name is `<deduplicated_symbol>` in the stack frame, the linker merged multiple functions with identical machine instructions into a single symbol. This optimization is called *code deduplication*. Xcode turns it on by default in release builds and turns it off in debug builds. To reveal all the functions the deduplicated symbol refers to, add the `-dedup` flag to the `atos` command.

After you find the binary name, look for a matching entry in the list of binary images at the bottom of the crash report. Note its architecture and load address. If you symbolicate the kernel address space, use the `textExecAddress` instead of the load address. The following binary images section shows an `arm64` architecture and a `0x10459c000` load address for `TouchCanvas`:

![A crash report with the binary name, address to symbolicate, and the Binary images section highlighted.](/images/com.apple.Xcode/adding-identifiable-symbol-names-to-a-crash-report-03@2x.png)

Locate the `.dSYM` file for the binary. The file is a macOS bundle that contains the DWARF debug symbol file. When invoking `atos`, provide the path to this file, not just to the `.dSYM` bundle. If you can’t find the `.dSYM`, follow the steps in [`Locating a missing debug symbol file`](locating-a-missing-debug-symbol-file.md) to find the one that matches the binary image’s build UUID.

After you gather the architecture, the `.dSYM` file’s path, the load or `textExecAddress`, and the address to symbolicate, pass them to the following `atos` command:

```shell
% atos -arch <binary-architecture> -o <path-to-dSYM>/Contents/Resources/DWARF/<binary-name> [-l <load-address>] [-textExecAddress <address>] [-i] [-dedup] <addresses-to-symbolicate> 

```

The compiler may inline functions as an optimization and omit their stack frames from the crash report. To reveal any inlined functions in the expanded backtrace, include the `-i` flag before the address. If symbol information is available, `atos` resolves the address to a function name and displays the source file name and line number, like this:

```shell
% atos -arch arm64 -o TouchCanvas.app.dSYM/Contents/Resources/DWARF/TouchCanvas -l 0x10459c000 -i 0x1045a4610
@objc ViewController.touchesEstimatedPropertiesUpdated(_:) (in TouchCanvas) (/<compiler-generated>:0)

```

## See Also

- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)
  Find patterns in crash reports that identify common problems, and investigate the issue based on the pattern.
- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.
- [Examining the fields in a crash report](examining-the-fields-in-a-crash-report.md)
  Understand the structure of a crash report and the information each field contains.
- [Interpreting the JSON format of a crash report](interpreting-the-json-format-of-a-crash-report.md)
  Understand the structure and properties of the objects the system includes in the JSON of a crash report.
- [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)
  Learn what the exception type tells you about why your app crashed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adding-identifiable-symbol-names-to-a-crash-report)*