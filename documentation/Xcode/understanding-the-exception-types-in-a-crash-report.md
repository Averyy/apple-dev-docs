# Understanding the exception types in a crash report

**Framework**: Xcode

Learn what the exception type tells you about why your app crashed.

#### Overview

The exception type in a crash report describes how the app terminated. It’s a key piece of information that guides how to investigate the source of the problem.

```other
Exception Type: EXC_BAD_ACCESS (SIGSEGV)
```

Crash reports record language exception information separately, including language exceptions thrown by an API or language features in Objective-C or C++.

## Topics

### Exceptions
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
- [EXC_RESOURCE](exc_resource.md)
  The operating system stopped the process because the process exceeded a limit on resource consumption, like CPU time or memory.

## See Also

- [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md)
  Replace hexadecimal addresses in a crash report with function names and line numbers that correspond to your app’s code.
- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)
  Find patterns in crash reports that identify common problems, and investigate the issue based on the pattern.
- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.
- [Examining the fields in a crash report](examining-the-fields-in-a-crash-report.md)
  Understand the structure of a crash report and the information each field contains.
- [Interpreting the JSON format of a crash report](interpreting-the-json-format-of-a-crash-report.md)
  Understand the structure and properties of the objects the system includes in the JSON of a crash report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/understanding-the-exception-types-in-a-crash-report)*