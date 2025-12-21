# EXC_RESOURCE

**Framework**: Xcode

The operating system stopped the process because the process exceeded a limit on resource consumption, like CPU time or memory.

#### Overview

If the `Exception Note` field contains `NON-FATAL CONDITION`, this means the operating system generated a crash report without actually terminating the process. The `Exception Message` field describes the amount of resources consumed over a specific time interval.

The crash report lists the specific resource in the `Exception Subtype` field:

Excessive wake-ups can come from calling thread-to-thread communication APIs more often than expected; these APIs include [`perform(_:on:with:waitUntilDone:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/perform(_:on:with:waitUntilDone:)), [`async(execute:)`](https://developer.apple.com/documentation/Dispatch/DispatchQueue/async(execute:)), and [`dispatch_async`](https://developer.apple.com/documentation/Dispatch/dispatch_async). Because the communication that triggers this exception is happening so frequently, crash reports usually include multiple background threads with very similar backtraces that indicate the origin of the thread communication. See [`Modernizing Grand Central Dispatch Usage`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2017/706/) for how to manage concurrent workloads more efficiently.

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
- [EXC_CRASH (SIGABRT)](sigabrt.md)
  The process terminated because it received an abort signal.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/exc_resource)*