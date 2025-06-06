# Addressing language exception crashes

**Framework**: Xcode

Identify the signs of a language exception, and address the crashes caused by uncaught language exceptions.

#### Overview

Language exceptions, such as those from Objective-C, indicate programming errors discovered at runtime, such as accessing an array with an index that’s out-of-bounds or not implementing a required method of a protocol. To determine whether a crash is due to a language exception, first confirm that the crash report contains this pattern:

```other
Exception Type:  EXC_CRASH (SIGABRT)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note:  EXC_CORPSE_NOTIFY
```

A crash due to a language exception that isn’t caught has a `Last Exception Backtrace` in the crash report. Verify this backtrace is present to confirm the crash is due to a language exception.

> **Note**: Exception backtraces to the code throwing the exception aren’t provided for C++ exceptions.

Exception backtraces to the code throwing the exception aren’t provided for C++ exceptions.

##### Identify the Api Throwing the Exception

In the `Last Exception Backtrace`, the operating system records the full backtrace of function calls leading to the exception. This backtrace ends with frames that make it clear a language exception was thrown. Further down the backtrace, you’ll find key information about what method threw the exception, and what part of your code called the method that threw the exception. For example:

```other
Last Exception Backtrace:
0   CoreFoundation                    0x1bf596a48 __exceptionPreprocess + 220
1   libobjc.A.dylib                   0x1bf2bdfa4 objc_exception_throw + 55
2   CoreFoundation                    0x1bf49b0ec -[NSException raise] + 11
3   Foundation                        0x1bf879170 -[NSObject+ 205168 (NSKeyValueCoding) setValue:forKey:] + 311
4   UIKitCore                         0x1c2ffa0b4 -[UIViewController setValue:forKey:] + 99
5   UIKitCore                         0x1c32c1234 -[UIRuntimeOutletConnection connect] + 123
6   CoreFoundation                    0x1bf470f3c -[NSArray makeObjectsPerformSelector:] + 251
7   UIKitCore                         0x1c32be3a4 -[UINib instantiateWithOwner:options:] + 1967
8   UIKitCore                         0x1c3000f18 -[UIViewController _loadViewFromNibNamed:bundle:] + 363
9   UIKitCore                         0x1c30019a4 -[UIViewController loadView] + 175
10  UIKitCore                         0x1c3001c5c -[UIViewController loadViewIfRequired] + 171
11  UIKitCore                         0x1c3002360 -[UIViewController view] + 27
12  UIKitCore                         0x1c3017a98 -[UIViewController _setPresentationController:] + 107
13  UIKitCore                         0x1c30108a4 -[UIViewController _presentViewController:modalSourceViewController:presentationController:animationController:interactionController:completion:] + 1343
14  UIKitCore                         0x1c30122b8 -[UIViewController _presentViewController:withAnimationController:completion:] + 4255
15  UIKitCore                         0x1c3014794 __63-[UIViewController _presentViewController:animated:completion:]_block_invoke + 103
16  UIKitCore                         0x1c3014c90 -[UIViewController _performCoordinatedPresentOrDismiss:animated:] + 507
17  UIKitCore                         0x1c30146e4 -[UIViewController _presentViewController:animated:completion:] + 195
18  UIKitCore                         0x1c301494c -[UIViewController presentViewController:animated:completion:] + 159
19  MyCoolApp                         0x104e8b1ac MyViewController.viewDidLoad() (in MyCoolApp) (MyViewController.swift:35)
```

In this example backtrace, the operating system threw an exception in frames 0-2. Frame 3 raised the exception because it couldn’t complete the connection of the `@IBOutlet` properties defined in an Interface Builder file loaded into memory in frames 4-7. Frames 8-17 show UIKit preparing to present this view defined in Interface Builder. Frame 18 shows this crash started from the app calling [`present(_:animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/present(_:animated:completion:)), called from [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad()) in frame 19. Frame 19 is a key piece of information for investigating this crash; it tells you to determine which Interface Builder file contains the problem by inspecting the source code near line 35 in `MyViewController.swift`.

> ❗ **Important**: If the API throwing the exception is [`doesNotRecognizeSelector(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/doesNotRecognizeSelector(_:)):, the crash may be due to a zombie object. See [`Investigating crashes for zombie objects`](investigating-crashes-for-zombie-objects.md) for additional information.

If the API throwing the exception is [`doesNotRecognizeSelector(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/doesNotRecognizeSelector(_:)):, the crash may be due to a zombie object. See [`Investigating crashes for zombie objects`](investigating-crashes-for-zombie-objects.md) for additional information.

##### Check the Exception Message

The uncaught exception handler provided by the operating system logs the exception message to the console before terminating the process. If you reproduce a crash resulting from a language exception with the Xcode debugger attached to your app, you can see this message:

```other
Application Specific Information:
*** Terminating app due to uncaught exception 'NSUnknownKeyException', 
    reason: '[<MyCoolApp.MyViewController 0x105510d50> setValue:forUndefinedKey:]: 
    this class is not key value coding-compliant for the key refreshButton.'
```

Continuing the example in [`Identify the API throwing the exception`](addressing-language-exception-crashes#Identify-the-API-throwing-the-exception.md), this exception message fills in details not visible in the exception backtrace — the Interface Builder file has an outlet named `refreshButton`, but the `MyViewController` class doesn’t declare an `@IBOutlet` property by that name.

The crash report excludes the exception message for some errors to prevent disclosing private information about the person using the app. The crash report includes exception messages for many of the common cases of language exceptions your app generates through its use of framework APIs. For more about these exceptions, see [`Reading an exception message`](reading-an-exception-message.md).

> **Note**: [`AppKit`](https://developer.apple.com/documentation/AppKit) apps have a default exception handler that catches all language exceptions raised by code run from its run loop. It logs the exception message and then allows the app to continue running.

[`AppKit`](https://developer.apple.com/documentation/AppKit) apps have a default exception handler that catches all language exceptions raised by code run from its run loop. It logs the exception message and then allows the app to continue running.

If you can reproduce a language exception crash, set an exception breakpoint to pause execution and inspect your app’s state with Xcode’s debugger, as described in [`Pause execution when events occur`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devfeaa874d0). To automatically print the exception message when the exception breakpoint pauses execution, add an action to the exception breakpoint that runs a debugger command:

```other
po $arg1
```

##### Address Crashes From a System Language Exception

After identifying the operating system’s API throwing the exception, consult the documentation for that API to determine what conditions trigger the exception. Also try to reproduce the crash with the Xcode debugger attached to get the additional information about the exception in the console, using the frames in the backtrace as a guide to the specific code you need to test.

If you can’t reproduce the crash, use all of the thread backtraces (not just the exception backtrace) as clues about what your app was doing at the time it crashed, and think about what that information says about your app’s state. Use those clues as a starting point for addressing the crash.

##### Handle Language Exceptions Thrown By Your Apps Code

64-bit versions of iOS and iPadOS use a zero-cost exception implementation, where every function has additional data that describes how to unwind the stack, or exit each stack frame, if a function throws an exception. If the thrown exception encounters a stack frame that doesn’t have unwind data, exception handling can’t proceed and the process halts. There might be an exception handler further up the stack, but without the unwind data for a frame, there’s no way to reach the exception handler from the stack frame throwing the exception.

If you find that exceptions thrown by your app within an exception handling domain aren’t caught, verify that the build settings for your app and libraries allow the compiler to create the unwind tables:

- Don’t specify the `-no_compact_unwind` flag.
- Specify the `-funwind-tables` flag if you’re including plain C code.

## See Also

- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.
- [Addressing crashes from Swift runtime errors](addressing-crashes-from-swift-runtime-errors.md)
  Identify the signs of a Swift runtime error, and address the crashes runtime errors cause.
- [Reading an exception message](reading-an-exception-message.md)
  Understand and address the common reasons apps crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/addressing-language-exception-crashes)*