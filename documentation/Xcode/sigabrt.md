# EXC_CRASH (SIGABRT)

**Framework**: Xcode

The process terminated because it received an abort signal.

#### Overview

Typically, the `SIGABRT` signal is sent because the process called the `abort()` function, such as when an app encounters an uncaught Objective-C or C++ language exception. [`Addressing language exception crashes`](addressing-language-exception-crashes.md) explains how to handle uncaught language exceptions in more detail. This signal can also come from another process that has the privileges to manage this process’ lifetime, and sent a `SIGABRT` because this process misbehaved in a detectable manner.

If the signal wasn’t sent because of a language exception, look at the crashed thread’s backtrace to determine if code in the process called `abort()`. For more information about the `abort()` function from the C standard library, enter `man 3 abort` in Terminal to view the `abort(3)` man page.

If an app extension takes too much time to initialize, the operating system sends a `SIGABRT` to the app extension process. These crashes include an `Exception Subtype` field with the value `LAUNCH_HANG`. Because extensions don’t have a `main` function, any time spent initializing occurs within static constructors and [`load()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/load()) methods that are present in your extension and dependent libraries. Although the exception information is different in a watchdog termination, investigate the `LAUNCH_HANG` using the same techniques discussed in [`Addressing watchdog terminations`](addressing-watchdog-terminations.md).

## See Also

- [EXC_ARITHMETIC](exc_arithmetic.md)
  An arithmetic problem terminated the process, often because of division by zero or a floating-point error.
- [EXC_BAD_ACCESS](exc_bad_access.md)
  A bad access to memory terminated the process.
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md)
  A bus error terminated the process, often because the process tried to access a misaligned or invalid address in memory, or due to a pointer authentication failure.
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md)
  A memory segmentation fault terminated the process, often because the process tried to access an invalid or out-of-bounds address in memory.
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md)
  A trace trap or invalid CPU instruction interrupted the process, often because the process violated a requirement or timeout.
- [EXC_CRASH](exc_crash.md)
  The process crashed.
- [EXC_CRASH (SIGKILL)](sigkill.md)
  The operating system terminated the process, often because a background task violated a requirement, device resources were limited, or the user force quit the app.
- [EXC_CRASH (SIGQUIT)](sigquit.md)
  Another processes terminated the process, often because the process violated a requirement or timeout.
- [EXC_CRASH (SIGSYS)](sigsys.md)
  A bad argument to a system call terminated the process.
- [EXC_CRASH (SIGTERM)](sigterm.md)
  A software termination signal terminated the process.
- [EXC_GUARD](exc_guard.md)
  The process violated a guarded resource protection, often related to file descriptors.
- [EXC_RESOURCE](exc_resource.md)
  The operating system stopped the process because the process exceeded a limit on resource consumption, like CPU time or memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/sigabrt)*