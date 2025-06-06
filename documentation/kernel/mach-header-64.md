# mach_header_64

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct mach_header_64 {
    ...
};
```

## Topics

### Instance Properties
- [cpusubtype](mach_header_64/1525740-cpusubtype.md)
  An integer specifying the exact model of the CPU. To run on all PowerPC processors supported by the macOS kernel, this should be set to `CPU_SUBTYPE_POWERPC_ALL`.
- [cputype](mach_header_64/1525741-cputype.md)
- [filetype](mach_header_64/1525785-filetype.md)
- [flags](mach_header_64/1525810-flags.md)
  An integer containing a set of bit flags that indicate the state of certain optional features of the Mach-O file format. These are the masks you can use to manipulate this field:
- [magic](mach_header_64/1525718-magic.md)
  An integer containing a value identifying this file as a 64-bit Mach-O file. Use the constant `MH_MAGIC_64` if the file is intended for use on a CPU with the same endianness as the computer on which the compiler is running. The constant `MH_CIGAM_64` can be used when the byte ordering scheme of the target machine is the reverse of the host CPU.
- [ncmds](mach_header_64/1525341-ncmds.md)
- [reserved](mach_header_64/1525781-reserved.md)
- [sizeofcmds](mach_header_64/1525364-sizeofcmds.md)

## See Also

- [mach_atm_subaid_t](mach_atm_subaid_t.md)
- [mach_core_details](mach_core_details.md)
- [mach_core_fileheader](mach_core_fileheader.md)
- [mach_header](mach_header.md)
- [mach_bridge_regwrite_timestamp_func_t](mach_bridge_regwrite_timestamp_func_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/mach_header_64)*