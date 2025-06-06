# EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)

**Framework**: Xcode

A trace trap or invalid CPU instruction interrupted the process, often because the process violated a requirement or timeout.

#### Overview

A trace trap gives an attached debugger the chance to interrupt the process at a specific point in its execution. On ARM processors, this appears as `EXC_BREAKPOINT (SIGTRAP). `On `x86_64` processors, this appears as `EXC_BAD_INSTRUCTION (SIGILL)`.

The Swift runtime uses trace traps for specific types of unrecoverable errors—see [`Addressing crashes from Swift runtime errors`](addressing-crashes-from-swift-runtime-errors.md) for information on those errors. Some lower-level libraries, such as [`Dispatch`](https://developer.apple.com/documentation/Dispatch), trap the process with this exception upon encountering an unrecoverable error, and log additional information about the error in the `Additional Diagnostic Information` section of the crash report. See [`Diagnostic messages`](examining-the-fields-in-a-crash-report#Diagnostic-messages.md) for information about those messages.

If you want to use the same technique in your own code for unrecoverable errors, call the [`fatalError(_:file:line:)`](https://developer.apple.com/documentation/Swift/fatalError(_:file:line:)) function in Swift, or the `__builtin_trap()` function in C. These functions allow the system to generate a crash report with thread backtraces that show how you reached the unrecoverable error.

An illegal CPU instruction means the program’s executable contains an instruction that the processor doesn’t implement or can’t execute. For example, the following program tries to perform the CPU instruction `0x00000001`, which isn’t a valid instruction on Apple silicon:

```c
#include <stdint.h>

int main(int argc, char **argv) {
    static const uint32_t sTest[] = {
        0x00000001,
    };
    typedef void (*FuncPtr)(void);
    FuncPtr f = (FuncPtr) sTest;
    f();
    return 0;
}
```

## See Also

- [EXC_ARITHMETIC](exc_arithmetic.md)
  An arithmetic problem terminated the process, often because of division by zero or a floating-point error.
- [EXC_BAD_ACCESS](exc_bad_access.md)
  A bad access to memory terminated the process.
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md)
  A bus error terminated the process, often because the process tried to access a misaligned or invalid address in memory, or due to a pointer authentication failure.
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md)
  A memory segmentation fault terminated the process, often because the process tried to access an invalid or out-of-bounds address in memory.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/sigtrap_sigill)*