# Writing ARMv7 code for iOS

**Framework**: Xcode

Create ARMv7 assembly language instructions that adhere to the application binary interface (ABI) that iOS supports.

#### Overview

The calling conventions for the ARMv7 and ARMv6 environments are nearly identical. As a result, any app you build for the ARMv7 environment is capable of running in the ARMv6 environment and vice versa. However, some ARMv7 environment features deviate from, or extend, the features of the ARMv6 environment.

##### Preserve Specific Registers in Armv7

The ARMv7 architecture preserves the same registers as the ARMv6 architecture, except for the changes and additions in the following table:

| Type | Name | Preserved | Notes |
| --- | --- | --- | --- |
| VFP register | D0-D7 | No | Also known as Q0-Q3 on ARMv7. These registers are accessible from Thumb mode on ARMv7. |
|  | D8-D15 | Yes | Also known as Q4-Q7 on ARMv7. These registers are accessible from Thumb mode on ARMv7. |
|  | D16-D31 | No | Also known as Q8-Q15. These registers are available only in ARMv7. |

For additional register preservation guidance, see [`Preserve specific registers in ARMv6`](writing-armv6-code-for-ios#Preserve-specific-registers-in-ARMv6.md).

##### Generate Arm or Thumb Code From the Same Assembly

The version of Thumb in ARMv7 is compatible with ARM assembly instructions.  Specifically, Thumb is capable of saving and restoring the contents of the VFP registers, and ARMv7 assembly uses a unified set of mnemonics.

The following example shows a prolog that saves key registers, including several VFP registers. It also allocates 36 bytes for local storage.

```other
push add  {r4-r7, lr}     // save LR, R7, R4-R6.
add       r7, sp, #12     // Adjust R7 to point to saved R7.
push      {r8, r10, r11}  // Save remaining GPRs (R8, R10, R11).
vstmdb    sp!, {d8-d15}   // Save VFP/Advanced SIMD registers D8 
                          // (aka S16-S31, Q4-Q7).
sub       sp, sp, #36     // Allocate space for local storage.
```

The following example shows the epilog that restores the registers saved by the preceding prolog:

```other
add       sp, sp, #36     // Deallocate space for local storage.
vldmia    sp!, {d8-d15}   // Restore VFP/Advanced SIMD registers.
pop       {r8, r10, r11}  // Restore R8-R11.
pop       {r4-r7, pc}     // Restore R4-R6, saved R7, and 
                          // return to saved LR
```

## See Also

- [Writing ARMv6 code for iOS](writing-armv6-code-for-ios.md)
  Create ARMv6 assembly language instructions that adhere to the application binary interface (ABI) that iOS supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/writing-armv7-code-for-ios)*