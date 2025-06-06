# dylib_module_64

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct dylib_module_64 {
    ...
};
```

## Topics

### Instance Properties
- [iextdefsym](dylib_module_64/1525313-iextdefsym.md)
- [iextrel](dylib_module_64/1525545-iextrel.md)
- [iinit_iterm](dylib_module_64/1525825-iinit_iterm.md)
- [ilocalsym](dylib_module_64/1525280-ilocalsym.md)
- [irefsym](dylib_module_64/1525769-irefsym.md)
- [module_name](dylib_module_64/1525436-module_name.md)
- [nextdefsym](dylib_module_64/1525515-nextdefsym.md)
- [nextrel](dylib_module_64/1525924-nextrel.md)
- [ninit_nterm](dylib_module_64/1525918-ninit_nterm.md)
  Contains both the number of pointers in the module initialization (the low 16 bits) and the number of pointers in the module termination section (the high 16 bits) for this module.
- [nlocalsym](dylib_module_64/1525930-nlocalsym.md)
- [nrefsym](dylib_module_64/1525420-nrefsym.md)
- [objc_module_info_addr](dylib_module_64/1525679-objc_module_info_addr.md)
- [objc_module_info_size](dylib_module_64/1525744-objc_module_info_size.md)

## See Also

- [dyld_info_command](dyld_info_command.md)
- [dyld_kernel_image_info_array_t](dyld_kernel_image_info_array_t.md)
- [dyld_uuid_info_32](dyld_uuid_info_32.md)
- [dyld_uuid_info_64](dyld_uuid_info_64.md)
- [dyld_uuid_info_64_v2](dyld_uuid_info_64_v2.md)
- [dylib](dylib.md)
- [dylib_command](dylib_command.md)
- [dylib_module](dylib_module.md)
- [dylib_reference](dylib_reference.md)
- [dylib_table_of_contents](dylib_table_of_contents.md)
- [dylinker_command](dylinker_command.md)
- [dysymtab_command](dysymtab_command.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/dylib_module_64)*