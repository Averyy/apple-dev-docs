# Investigating memory access crashes

**Framework**: Xcode

Identify crashes that arise from memory access issues, and investigate the cause of the crash.

#### Overview

A crash due to a memory access issue occurs when an app uses memory in an unexpected way. Memory access problems have numerous causes, such as dereferencing a pointer to an invalid memory address, writing to read-only memory, or jumping to an instruction at an invalid address. These crashes are most often identified by the `EXC_BAD_ACCESS (SIGSEGV)` or `EXC_BAD_ACCESS (SIGBUS)` exceptions in the crash report:

```other
Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Subtype: KERN_INVALID_ADDRESS at 0x0000000000000000
```

On macOS, bad memory access crashes are occasionally identified only by a signal, such as `SIGSEGV`, `SEGV_MAPERR`, or `SEGV_NOOP`:

```other
Exception Type: SIGSEGV
Exception Codes: SEGV_MAPERR at 0x41e0af0c5ab8
```

Xcode provides several tools that can help identify the source of a memory access issue. Further analysis of each section in the crash report may provide further insight and clues to help you diagnose the problem.

##### Investigate the Crash with Xcode

Once you’ve identified that a crash report is for a memory access issue through the exception type, use Xcode to continue your investigation. Xcode contains a suite of debugging tools you can use to identify memory access issues as your app runs. These tools are most effective when your tests execute as many code branches in the app as possible:

- Address Sanitizer
- Undefined Behavior Sanitizer
- Thread Sanitizer

If your app contains code in Objective-C, C, or C++, run the static analyzer, and fix all issues it discovers. The static analyzer analyzes your app’s code at build time, and identifies common programming mistakes, including some types of memory management issues. See [`Analyze your code for potential flaws`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devb7babe820).

Beyond the exception type in the crash report, other sections of the crash report may contain additional clues that suggest applying additional debugging tools. For example, if a zombie object caused the crash, telltale signs are in the crash report. See [`Check the crashed thread’s backtrace for clues about the source of the memory access issue`](investigating-memory-access-crashes#Check-the-crashed-threads-backtrace-for-clues-about-the-source-of-the-memory-access-issue.md) for information on the specific clues.

For difficult to diagnose memory access crashes, the malloc debugging features, such as Guard Malloc, can help. See [`Enabling the Malloc Debugging Features`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/MallocDebug.html#//apple_ref/doc/uid/20001884) for information about these tools. You enable these tools through the Xcode scheme editor, as described by [`Run your app with sanitizers, API checks, and memory management diagnostics`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devcef23c572).

##### Examine the Exception Subtype to Determine Why Access Was Invalid

The `Exception Subtype` field in the crash report contains a `kern_return_t` value describing the error and the address of the memory that was incorrectly accessed, such as:

```other
Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Subtype: KERN_INVALID_ADDRESS at 0x0000000000000000
```

On macOS, the `Exception Codes` field contains the exception subtype:

```other
Exception Type:        EXC_BAD_ACCESS (SIGBUS)
Exception Codes:       KERN_MEMORY_ERROR at 0x00000001098c1000
```

There are several exception subtypes:

- `KERN_INVALID_ADDRESS`. The crashed thread accessed unmapped memory, either by accessing data or an instruction fetch. [`Identify the type of memory access that caused the issue`](investigating-memory-access-crashes#Identify-the-type-of-memory-access-that-caused-the-issue.md) describes how to tell the difference.
- `KERN_PROTECTION_FAILURE`. The crashed thread tried to use a valid memory address that’s protected. Some types of protected memory include read-only memory regions, or nonexecutable memory regions. See [`Use VM Region Info to locate the memory in your app’s address space`](investigating-memory-access-crashes#Use-VM-Region-Info-to-locate-the-memory-in-your-apps-address-space.md) for how to distinguish the type of protected memory.
- `KERN_MEMORY_ERROR`. The crashed thread tried to access memory that couldn’t return data at that moment, such as a memory-mapped file that became unavailable.
- `EXC_ARM_DA_ALIGN`. The crashed thread tried to access memory that isn’t appropriately aligned. This exception code is rare because 64-bit ARM CPUs work with misaligned data. However, you may see this exception subtype if the memory address is both misaligned and located in an unmapped memory region. You may have other crash reports that show a memory access issue with a different exception subtype, which are likely caused by the same underlying memory access issue.

The `arm64e` CPU architecture uses pointer authentication codes with cryptographic signatures to detect and guard against unexpected changes to pointers in memory. A crash due to a possible pointer authentication failure uses the `KERN_INVALID_ADDRESS` exception subtype with an additional message on the end:

```other
Exception Type:  EXC_BAD_ACCESS (SIGBUS)
Exception Subtype: KERN_INVALID_ADDRESS at 0x00006f126c1a9aa0 -> 0x000000126c1a9aa0 (possible pointer authentication failure)
```

An invalid memory access, where high-order bits are erroneously set, can look like a pointer authentication failure, even if the cause is due to a memory corruption problem in the app.

See [`Preparing your app to work with pointer authentication`](https://developer.apple.com/documentation/Security/preparing-your-app-to-work-with-pointer-authentication) for more information about pointer authentication.

##### Use Vm Region Info to Locate the Memory in Your Apps Address Space

The `VM Region Info` field of the crash report shows the location of the specific memory that your app incorrectly accessed in relation to other sections of the app’s address space. Consider this example:

```other
Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Subtype: KERN_INVALID_ADDRESS at 0x0000000000000000
VM Region Info: 0 is not in any region.  Bytes before following region: 4307009536
      REGION TYPE                      START - END             [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
--->  
      __TEXT                 0000000100b7c000-0000000100b84000 [   32K] r-x/r-x SM=COW  ...pp/MyGreatApp
```

Here, a dereference to unmapped memory triggered the crash, at `0x0000000000000000`. This is an invalid address, specifically a `NULL` pointer, so the exception subtype indicates this with the `KERN_INVALID_ADDRESS` value. The `VM Region Info` field shows the location of this invalid address is 4,307,009,536 bytes before a valid region of memory in the app’s address space.

Consider a different example, for a `KERN_PROTECTION_FAILURE`:

```other
Exception Type:  EXC_BAD_ACCESS (SIGBUS)
Exception Subtype: KERN_PROTECTION_FAILURE at 0x000000016c070a30
VM Region Info: 0x16c070a30 is in 0x16c070000-0x16c074000;  bytes after start: 2608  bytes before end: 13775
      REGION TYPE                      START - END             [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      Stack                  000000016bfe8000-000000016c070000 [  544K] rw-/rwx SM=COW  thread 12
--->  STACK GUARD            000000016c070000-000000016c074000 [   16K] ---/rwx SM=NUL  ...for thread 11
      Stack                  000000016c074000-000000016c0fc000 [  544K] rw-/rwx SM=COW  thread 11
```

In this example, the dereferenced memory address is `0x000000016c070a30`, with the region containing this memory address identified by the arrow. The address is located in a special memory region called the stack guard, which is a memory region that buffers the stack of a thread from the stack of another thread. The `PRT` column shows the current permission attributes for the memory regions, with `r` indicating the memory is readable, `w` indicating the memory is writable, and `x` indicating the memory is executable.

Because the stack guard region has no permissions, all memory accesses to this region are invalid, and the crash report is identifying this memory access as a violation of the memory protection attributes. The stack guard is just one example of protected memory—there are others types of protected memory regions, with different combinations of the protection attributes.

See [`Interpreting vmmap’s Output`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/VMPages.html#//apple_ref/doc/uid/20001985-97652) for more information on the `VM Region Info` field.

##### Check the Crashed Threads Backtrace for Clues About the Source of the Memory Access Issue

Consult the crashed thread’s backtrace for clues on where the memory access issue is occurring. Some types of memory access issues, such as dereferencing a `NULL` pointer, are easy to identify when looking at the backtrace and comparing it to the source code. Other memory access issues are identified by the stack frame at the top of the crashed thread’s backtrace:

- If [`objc_msgSend`](https://developer.apple.com/documentation/ObjectiveC/objc_msgSend), `objc_retain`, or `objc_release` is at the top of the backtrace, the crash is due to a zombie object. See [`Investigating crashes for zombie objects`](investigating-crashes-for-zombie-objects.md).
- If `gpus_ReturnNotPermittedKillClient` is at the top of the backtrace, the operating system terminated the process because it attempted to do rendering with OpenGL ES while in the background. To resolve a crash with this symbol in the backtrace, migrate your OpenGL ES code to Metal. See [`Migrating OpenGL code to Metal`](https://developer.apple.com/documentation/Metal/migrating-opengl-code-to-metal).

In other cases, the cause of a memory access issue isn’t present in the backtrace.  occurs when a memory location is unexpectedly modified. After this modification, another part of your app may crash when it tries to use that memory location. The backtrace shows the code accessing the modified memory, but not the code that unexpectedly modified the memory. The unexpected modification may have occurred a long time before the crash, so the source of the issue isn’t visible in the backtrace. If you have numerous crash reports with signs of a memory access issue, but with different backtraces, you may have a memory corruption issue. The information in [`Investigate the crash with Xcode`](investigating-memory-access-crashes#Investigate-the-crash-with-Xcode.md) can help identify the source of the memory corruption.

##### Identify the Type of Memory Access That Caused the Issue

There are two categories of memory access issues: invalid memory fetches and invalid instruction fetches. An  occurs when code dereferences an invalid pointer. An  occurs when a function jumps to another function through a bad function pointer, or through a function call to an unexpected object. To determine which type of memory access issue caused a crash, focus on the , a register that contains the address of the instruction that caused the memory access exception. On ARM CPU architectures, this is the `pc` register. On the `x86_64` CPU architecture, this is the `rip` register.

If the program counter register isn’t the same as the exception address, the crash is due to an invalid memory fetch. For example, consider the following macOS crash report on an `x86_64` CPU:

```other
Exception Type:  SIGSEGV
Exception Codes: SEGV_MAPERR at 0x21474feae2c8
...
Thread 12 crashed with X86-64 Thread State:
   rip: 0x00007fff61f5739d    rbp: 0x00007000026c72c0    rsp: 0x00007000026c7248    rax: 0xe85e2965c85400b4 
   rbx: 0x00006000023ee2b0    rcx: 0x00007f9273022990    rdx: 0x00007000026c6d88    rdi: 0x00006000023ee2b0 
   rsi: 0x00007fff358aae0f     r8: 0x00000000000003ff     r9: 0x00006000023edbc0    r10: 0x000021474feae2b0 
   r11: 0x00007fff358aae0f    r12: 0x000060000237af10    r13: 0x00007fff61f57380    r14: 0x00006000023ee2b0 
   r15: 0x0000000000000006 rflags: 0x0000000000010202     cs: 0x000000000000002b     fs: 0x0000000000000000 
    gs: 0x0000000000000000 

```

The program counter register is `0x00007fff61f5739d`, which isn’t the same as the exception’s address of `0x21474feae2c8`. This crash is due to an invalid memory fetch.

If the program counter register is the same as the exception address, the crash is due to an invalid instruction fetch. For example, consider the following iOS crash report on an `arm64` CPU:

```other
Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Subtype: KERN_INVALID_ADDRESS at 0x0000000000000040
...
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   ???                               0x0000000000000040 0 + 64
...
Thread 0 crashed with ARM Thread State (64-bit):
    x0: 0x0000000000000002   x1: 0x0000000000000040   x2: 0x0000000000000001   x3: 0x000000016dcfe080
    x4: 0x0000000000000010   x5: 0x000000016dcfdc8f   x6: 0x000000016dcfdd80   x7: 0x0000000000000000
    x8: 0x000000010210d3c8   x9: 0x0000000000000000  x10: 0x0000000000000014  x11: 0x0000000102835948
   x12: 0x0000000000000014  x13: 0x0000000000000000  x14: 0x0000000000000001  x15: 0x0000000000000000
   x16: 0x000000010210c0b8  x17: 0x00000001021063b0  x18: 0x0000000000000000  x19: 0x0000000102402b80
   x20: 0x0000000102402b80  x21: 0x0000000204f6b000  x22: 0x00000001f6e6f984  x23: 0x0000000000000001
   x24: 0x0000000000000001  x25: 0x00000001fc47b690  x26: 0x0000000102304040  x27: 0x0000000204eea000
   x28: 0x00000001f6e78fae   fp: 0x000000016dcfdec0   lr: 0x00000001021063c4
    sp: 0x000000016dcfdec0   pc: 0x0000000000000040 cpsr: 0x40000000
   esr: 0x82000006 (Instruction Abort) Translation fault

Binary Images:
0x102100000 - 0x102107fff MyCoolApp arm64  <87760ecf8573392ca5795f0db63a44e2> /var/containers/Bundle/Application/686CA3F1-6CC5-4F84-8126-EE22D03BC161/MyCoolApp.app/MyCoolApp

```

In this example, the program counter register is `0x0000000000000040`, which matches the address reported in the Exception Subtype, indicating this crash is due to a bad instruction fetch. Because this is a bad instruction fetch, frame 0 in the backtrace doesn’t contain a running function, as indicated by the `???` and memory address instead of a symbol name in the backtrace. However, the link register, `lr`, contains the location the code would return to after a function call under normal circumstances. The value in the link register allows you trace the origin of the jump to a bad instruction pointer.

> **Note**: The `x86_64` CPU architecture stores return addresses on the stack, instead of in a link register, so you can’t trace the origin of the bad function pointer on `x86_64` CPUs.

The link register contains `0x00000001021063c4`, which is an instruction address in one of the binaries loaded in the app’s process. The Binary Images section of the crash report shows that this address is inside the `MyCoolApp` binary, because that address is in the range `0x102100000-0x102107fff` listed for that binary. With this information, you can use the `atos` command line tool with the `dSYM` file for the binary, and identify the corresponding code located at `0x00000001021063c4`:

```other
% atos -arch arm64 -o MyCoolApp.app.dSYM/Contents/Resources/DWARF/MyCoolApp -l 0x102100000 0x00000001021063c4
-[ViewController loadData] (in MyCoolApp) (ViewController.m:38)
```

[`Symbolicate the crash report with the command line`](adding-identifiable-symbol-names-to-a-crash-report#Symbolicate-the-crash-report-with-the-command-line.md) discusses how to use the `atos` command line tool in more detail.

## See Also

- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.
- [Investigating crashes for zombie objects](investigating-crashes-for-zombie-objects.md)
  Identify the signature of a zombie and investigate the cause of the crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/investigating-memory-access-crashes)*