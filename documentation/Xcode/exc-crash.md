# EXC_CRASH

**Framework**: Xcode

The process crashed.

#### Overview

For more specific information, see the article that corresponds to the accompanying signal:

- [`EXC_CRASH (SIGABRT)`](sigabrt.md)
- [`EXC_CRASH (SIGKILL)`](sigkill.md)
- [`EXC_CRASH (SIGQUIT)`](sigquit.md)
- [`EXC_CRASH (SIGSYS)`](sigsys.md)
- [`EXC_CRASH (SIGTERM)`](sigterm.md)

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
- [EXC_RESOURCE](exc_resource.md)
  The operating system stopped the process because the process exceeded a limit on resource consumption, like CPU time or memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/exc_crash)*