# Determining Instruction Set Characteristics

**Framework**: Kernel

Interrogate the system for details about the instruction set.

#### Overview

Use parameters with the [`sysctlbyname`](1387446-sysctlbyname.md) interface to check for the existence of Instruction Set Architecture (ISA) features available in Apple silicon and documented at [`Arm Architecture Reference Manual for A-profile architecture`](https://developer.apple.comhttps://developer.arm.com/documentation/ddi0487/latest). Implemented features have a parameter value of 1. Features that aren’t implemented have a parameter value of 0. Non-existent features return an error.

To verify that your CPU uses the ARM Instruction Set Architecture, use `hw.optional.arm64`. A value of 1 indicates that the platform uses the ARM ISA.

The following parameters provide information about the availability of advanced single instruction multiple data (SIMD) and floating point capabilties. These features are standard in Apple processors beginning with M1 and A7, and don’t need to be checked.

- **`hw.optional.AdvSIMD`**: General support for Advanced SIMD instructions. This parameter replaces `hw.optional.neon`.
- **`hw.optional.floatingpoint`**: General support for floating-point instructions.

##### 3915618

The following parameters provide information about SIMD and floating point support in the processor.

- **`hw.optional.AdvSIMD_HPFPCvt`**: Advanced SIMD half-precision conversion instructions. This parameter replaces `hw.optional.neon_hpfp`.
- **`hw.optional.arm.FEAT_BF16`**: Storage and arithmetic instructions of the Brain Floating Point (`BFloat16`) data type.
- **`hw.optional.arm.FEAT_DotProd`**: Advanced SIMD Int8 dot product instructions.
- **`hw.optional.arm.FEAT_FCMA`**: Floating-point complex number instructions. This parameter replaces `hw.optional.armv8_3_compnum`.
- **`hw.optional.arm.FEAT_FHM`**: Floating-point half-precision multiplication instructions. This parameter replaces `hw.optional.armv8_2_fhm`.
- **`hw.optional.arm.FEAT_FP16`**: General half-precision floating-point data processing instructions. This parameter replaces `hw.optional.neon_fp16.`
- **`hw.optional.arm.FEAT_FRINTTS`**: Floating-point to integral valued floating-point number rounding instructions.
- **`hw.optional.arm.FEAT_I8MM`**: Advanced SIMD Int8 matrix multiplication instructions.
- **`hw.optional.arm.FEAT_JSCVT`**: JavaScript conversion instruction.
- **`hw.optional.arm.FEAT_RDM`**: Advanced SIMD rounding double multiply accumulate instructions.

##### 3915619

The following parameters provide information about integer support in the processor.

- **`hw.optional.arm.FEAT_FlagM`**: Condition flag manipulation instructions.
- **`hw.optional.arm.FEAT_FlagM2`**: Enhancements to condition flag manipulation instructions.
- **`hw.optional.armv8_crc32`**: CRC32 instructions.

##### 3923651

The following parameters provide information about atomicity and memory capabilities.

- **`hw.optional.arm.FEAT_LRCPC`**: Load-acquire Release Consistency processor consistent (`RCpc`) instructions.
- **`hw.optional.arm.FEAT_LRCPC2`**: Load-acquire Release Consistency processor consistent (`RCpc`) instructions version 2.
- **`hw.optional.arm.FEAT_LSE`**: Atomic instructions to support large systems. This parameter replaces `hw.optional.armv8_1_atomics`.
- **`hw.optional.arm.FEAT_LSE2`**: Changes to single-copy atomicity and alignment requirements for loads and stores for large systems.

##### 3918855

The following parameters provide information about support for instructions that accelerate encryption and decryption in the processor.

- **`hw.optional.arm.FEAT_AES`**: Advanced SIMD AES instructions.
- **`hw.optional.arm.FEAT_PMULL`**: Advanced SIMD PMULL instructions.
- **`hw.optional.arm.FEAT_SHA1`**: Advanced SIMD SHA1 instructions.
- **`hw.optional.arm.FEAT_SHA256`**: Advanced SIMD SHA256 instructions.
- **`hw.optional.arm.FEAT_SHA512`**: Advanced SIMD SHA512 instructions. This parameter replaces `hw.optional.armv8_2_sha512`.
- **`hw.optional.arm.FEAT_SHA3`**: Advanced SIMD SHA-3 instructions. This parameter replaces `hw.optional.armv8_2_sha3`.

##### 3922605

The following parameters provide information about other capabiltiies in the processor.

- **`hw.optional.arm.FEAT_BTI`**: Instructions to guard against the execution of instructions that aren’t the intended target of a branch.
- **`hw.optional.arm.FEAT_DPB`**: Clean data cache by address to Point of Persistence DC CVAP instruction.
- **`hw.optional.arm.FEAT_DPB2`**: Clean data cache by address to Point of Deep Persistence DC CVADP instruction.
- **`hw.optional.arm.FEAT_ECV`**: Support for Enhanced Counter Virtualization, which enhances the Generic Timer architecture.
- **`hw.optional.arm.FEAT_SB`**: Barrier instruction to control speculation.
- **`hw.optional.arm.FEAT_SSBS`**: Instructions to control speculation of loads and stores.

## See Also

- [Determining system capabilities](1387446-sysctlbyname/determining_system_capabilities.md)
  Interrogate the system for processor, cache, and topology information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1387446-sysctlbyname/determining_instruction_set_characteristics)*