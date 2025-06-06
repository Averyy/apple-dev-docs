# Writing ARMv6 code for iOS

**Framework**: Xcode

Create ARMv6 assembly language instructions that adhere to the application binary interface (ABI) that iOS supports.

#### Overview

The ARMv6 specification defines the calling conventions for passing arguments and return values between two functions. You pass arguments on the runtime stack or in registers, and the called function returns results registers or in memory. For the most part, the ARMv6 specification adopts the same conventions as those defined in the Procedure Call Standard for the ARM Architecture (release 1.07). However, the ARMv6 specification deviates in the following ways:

- The stack is 4-byte aligned at the point of function calls.
- Data types larger than 4 bytes are 4-byte aligned.
- Register R7 serves as the frame pointer.
- Register R9 is a volatile scratch register.

> **Note**: Apple defines its own procedural programming interfaces for passing arguments to functions. Object-oriented languages may use different rules for their own method calls. For example, the conventions for C++ virtual functions are typically different than the conventions for C functions.

Apple defines its own procedural programming interfaces for passing arguments to functions. Object-oriented languages may use different rules for their own method calls. For example, the conventions for C++ virtual functions are typically different than the conventions for C functions.

The Procedure Call Standard for the ARM Architecture (AAPCS) is available at [`https://developer.arm.com`](https://developer.apple.comhttps://developer.arm.com).

##### Preserve Specific Registers in Armv6

The following table lists the ARM architecture registers and their volatility in procedure calls:

| Type | Name | Preserved | Notes |
| --- | --- | --- | --- |
| General-purpose register | R0-R3 | No | General-purpose registers available for use within a routine and between function calls. Pass arguments and results using these registers. |
|  | R4-R6 | Yes |  |
|  | R7 | Yes | The frame pointer. This register usually points to the previously saved stack frame and saved-link register. |
|  | R8 | Yes |  |
|  | R9 | No | A volatile scratch register in iOS 3 and later. |
|  | R10-R11 | Yes |  |
|  | R12 | No | The intra-procedure (IP) scratch register. The linker uses this register, and it is volatile across all function calls. However, you can use it as a scratch register between function calls. |
|  | R13 | Special | The stack pointer (SP). |
|  | R14 | Special | The link register (LR). This register stores the return address of a function call. |
|  | R15 | Special | The program counter (PC). |
| Program status register | CPSR | Special | The program status register. Function calls don’t preserve the condition bits (27-31) and GE bits (16-19). The E bit must remain zero (to indicate little-endian mode) when calling or returning from a function. Set the T bit only from a branch routine. Don’t modify any other bits. |
| VFP registers | D0-D7 | No | Also known as S0-S15. These registers are inaccessible from Thumb mode on ARMv6. |
|  | D8-D15 | yes | Also known as S16-S31. These registers are inaccessible from Thumb mode on ARMv6. |
| VFP status register | FPSCR | Special | The VFP status register. Function calls don’t preserve the condition code bits (28-31) and saturation bits (0-4). Modify the exception control bits (8-12), rounding mode bits (22-23), and flush-to-zero bit (24) only from routines that affect the app state, either directly or using framework API functions. The short vector length (16-18) and stride (20-21) bits must be zero on function entry and exit. Don’t modify any other bits. |

Consider the following additional behaviors with regard to register usage:

- The AAPCS document defines R7 as a general-purpose, nonvolatile register, but iOS uses it as a frame pointer. Failure to use R7 as a frame pointer prevents debugging and performance tools from generating valid backtraces.
- Some ARM environments refer to R11 with the mnemonic FP. In iOS, R11 is a general-purpose, nonvolatile register. To avoid confusion, iOS doesn’t use the term FP.
- Don’t access the VFP registers from Thumb mode in ARMv6. To access the VFP registers, run your code in ARM mode. In iOS, you can switch between ARM and Thumb mode only at function boundaries.

##### Handle Data Types and Data Alignment Properly

The following table lists the ANSI C scalar data types, their sizes, and their natural alignments in the ARMv6 environment. The natural alignment represents the default alignment for values of that type.

| Data type | Size (in bytes) | Natural alignment (in bytes) |
| --- | --- | --- |
| `BOOL`, `bool` | 1 | 1 |
| `unsigned char` | 1 | 1 |
| `char`, `signed char` | 1 | 1 |
| `unsigned short` | 2 | 2 |
| `signed short` | 2 | 2 |
| `unsigned int` | 4 | 4 |
| `signed int` | 4 | 4 |
| `unsigned long` | 4 | 4 |
| `signed long` | 4 | 4 |
| `unsigned long long` | 8 | 8 |
| `signed long long` | 8 | 8 |
| `float` | 4 | 4 |
| `double` | 8 | 4 |
| `long double` | 8 | 4 |
| pointer | 4 | 4 |

The ARMv6 environment uses little-endian byte ordering to store numeric and pointer data types. With this scheme, the least-significant byte is first, followed by the most-significant byte.

As standalone arguments, scalar data types use their natural alignment. When part of a composite data type (array, structure, or union), the system chooses the member with the largest alignment value and uses that value for the overall type alignment. An array assumes the same alignment as its elements. The overall size of a composite data type is a multiple of its alignment value, which might require extra padding to accomplish.

##### Configure Stack Frames Using Correct Conventions

In iOS, all subroutine call and return sequences must work in both the ARM and Thumb states. Specifically, you must use the appropriate `BLX` and `BX` instructions, and not the `MOV` instruction, for all calls to function pointers. The main difference between the ARM and Thumb instruction sets is how you set up the stacks and parameter lists.

The stack environment in ARMv6 has the following characteristics:

- It’s 4-byte aligned.
- It grows downward.
- It contains local variables and function parameters.

In the ARMv6 environment, the stack frame size is not fixed and the stack pointer (SP) points to the bottom of the stack. Stack frames contain the following areas:

- The  stores the arguments, or space for the arguments, that the caller passes to the called function. This area resides in the caller’s stack frame. The type of argument, and the availability of registers, defines whether the argument resides on the stack or in registers.
- The  contains the address of the caller’s next instruction.
- The  (optional) contains the base address of the caller’s stack frame.
- The  contains the values of registers that the callee must restore before it returns. For more information, see [`Preserve specific registers in ARMv6`](writing-armv6-code-for-ios#Preserve-specific-registers-in-ARMv6.md).
- The  contains each subroutine’s local variables.

![An illustration of the ARM stack, before and after a function call.](https://docs-assets.developer.apple.com/published/a357a5ca6ad94caa17f06172dc98d9fd/writing-armv6-code-for-ios-1%402x.png)

##### Create the Prolog and Epilog for a Function

When a function calls a subroutine, the subroutine must allocate its own stack frame. It accomplishes this task using a prolog, which is a section of code the compiler places before the body of the function. The compiler places an epilog at the end of the subroutine to restore the process to its prior state.

The prolog performs the following tasks:

1. It pushes the value of the link register (LR) onto the stack.
2. It pushes the value of the frame pointer (R7) onto the stack.
3. It sets the frame pointer (R7) to the value of the stack pointer (SP). (This step gives the debugger a way to find previous stack frames.)
4. It pushes appropriate register values onto the stack to preserve them. For more information, see [`Preserve specific registers in ARMv6`](writing-armv6-code-for-ios#Preserve-specific-registers-in-ARMv6.md).
5. It allocates space for local storage in the stack frame.

The epilog performs the following tasks:

1. It deallocates the local storage in the stack.
2. It restores any preserved registers.
3. It pops the saved frame pointer value and puts it back into R7.
4. It moves the saved link register (LR) value into the program counter (PC).

You don’t need to include any parts of the prolog or epilog that don’t apply to your code. For example, if a function doesn’t use high registers (R8, R10, R11) or nonvolatile VFP registers, you don’t need to save them. Leaf functions don’t need to use the stack at all, except to save nonvolatile registers.

The following example shows a prolog in ARM mode. This prolog saves the contents of the VFP registers and allocates an additional 36 bytes of local storage.

```other
stmfd    sp!, {r4-r7, lr}     // Save LR, R7, R4-R6.
add      r7, sp, #12          // Adjust R7 to point to saved R7.
stmfd    sp!, {r8, r10, r11}  // Save remaining GPRs (R8, R10, R11)
fstmfdd  sp!, {d8-d15}        // Save VFP registers D8-D15,
                              //  also known as S16-S31 or Q4-Q7.
sub      sp, sp, #36          // Allocate space for local storage
```

The following example shows the corresponding epilog in ARM mode. The epilog deallocates the local storage and restores the registers that the prolog saved.

```other
add      sp, sp, #36         // Deallocate local storage.
fldmfdd  sp!, {d8-d15}       // Restore VFP registers.
ldmdd    sp!, {r8, r10, r11} // Restore R8-R11.
ldmdd    sp!, {r4-r7, pc}    // Restore R4-R6, saved R7,
                             //  and return to saved LR.
```

The following example shows a prolog in Thumb mode. This prolog doesn’t save VFP registers because Thumb-1 cannot access those registers.

```other
push   {r4-r7, lr}     // Save Lr, R7, R4-R6.
mov    r6, r11         // Move high registers to low registers, so
mov    r5, r10         //  they can be saved. (Skip this part if
mov    r4, r8          //  the routine doesn’t use R8, R10, or R11.)
push   {r4-r6)         // Save R8, R10, R11 (now in R4-R6).
add    r7, sp, #24     // Adjust R7 to point to saved R7.
sub    sp, #36         // Allocate space for local storage.
```

The following example shows the corresponding epilog in Thumb mode. This example restores the registers the prolog saved.

```other
add    sp, #36         // Deallocate space for local storage
pop    {r4-r6}         // Pop R8, R10, R11
mov    r8, r4          // Restore high registers.
mov    r10, r5
mov    r11, r6
pop    {r4-r7, pc)     // Restore R4-R6, saved R7, and
                       //  return to saved LR.

```

##### Pass Arguments to Functions and Handle Return Values

The compiler generally adheres to the argument passing rules in the AAPCS document, but the following items are worth noting:

- Typically, you place the first four scalar arguments into the core registers (R0, R1, R2, and R3), and place any remaining arguments on the stack. For exceptions, see the AAPCS document at [`https://developer.arm.com`](https://developer.apple.comhttps://developer.arm.com).
- Use 4-byte alignment for data types larger than 4 bytes in size.
- Use the Base Standard variant of the procedure call standard for floating-point arguments. In this variant, you pass floating-point and vector arguments in general-purpose registers (GPRs) instead of in VFP registers.

The compiler generally returns results according to the standard rules. Specifically, it returns most values in R0 unless the size of the return value warrants a different approach.

For complete details about argument-passing and return result behaviors, see the AAPCS document at [`https://developer.arm.com`](https://developer.apple.comhttps://developer.arm.com).

## See Also

- [Writing ARMv7 code for iOS](writing-armv7-code-for-ios.md)
  Create ARMv7 assembly language instructions that adhere to the application binary interface (ABI) that iOS supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/writing-armv6-code-for-ios)*