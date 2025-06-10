# Determining Instruction Set Characteristics

**Framework**: Kernel

Interrogate the system for details about the instruction set.

#### Overview

Use parameters with the [`sysctlbyname`](1387446-sysctlbyname.md) interface to check for the existence of Instruction Set Architecture (ISA) features available in Apple silicon and documented at [`Arm Architecture Reference Manual for A-profile architecture`](https://developer.apple.comhttps://developer.arm.com/documentation/ddi0487/latest). Implemented features have a parameter value of 1. Features that aren’t implemented have a parameter value of 0. Non-existent features return an error.

To verify that your CPU uses the ARM Instruction Set Architecture, use `hw.optional.arm64`. A value of 1 indicates that the platform uses the ARM ISA.

The following parameters provide information about the availability of advanced single instruction multiple data (SIMD) and floating point capabilties. These features are standard in Apple processors beginning with M1 and A7, and don’t need to be checked.

##### 3915618

The following parameters provide information about SIMD and floating point support in the processor.

##### 3915619

The following parameters provide information about integer support in the processor.

##### 3923651

The following parameters provide information about atomicity and memory capabilities.

##### 3918855

The following parameters provide information about support for instructions that accelerate encryption and decryption in the processor.

##### 3922605

The following parameters provide information about other capabiltiies in the processor.

## See Also

- [Determining system capabilities](1387446-sysctlbyname/determining_system_capabilities.md)
  Interrogate the system for processor, cache, and topology information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1387446-sysctlbyname/determining_instruction_set_characteristics)*