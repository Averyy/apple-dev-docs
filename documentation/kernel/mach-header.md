# mach_header

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct mach_header {
    ...
};
```

## Topics

### Instance Properties
- [cpusubtype](mach_header/1525896-cpusubtype.md)
- [cputype](mach_header/1525625-cputype.md)
- [filetype](mach_header/1525892-filetype.md)
- [flags](mach_header/1525711-flags.md)
- [magic](mach_header/1525759-magic.md)
  An integer containing a value identifying this file as a 32-bit Mach-O file. Use the constant `MH_MAGIC` if the file is intended for use on a CPU with the same endianness as the computer on which the compiler is running. The constant `MH_CIGAM` can be used when the byte ordering scheme of the target machine is the reverse of the host CPU.
- [ncmds](mach_header/1525650-ncmds.md)
- [sizeofcmds](mach_header/1525712-sizeofcmds.md)

## See Also

- [mach_atm_subaid_t](mach_atm_subaid_t.md)
- [mach_core_details](mach_core_details.md)
- [mach_core_fileheader](mach_core_fileheader.md)
- [mach_header_64](mach_header_64.md)
- [mach_bridge_regwrite_timestamp_func_t](mach_bridge_regwrite_timestamp_func_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/mach_header)*