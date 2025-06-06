# dylib_module

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct dylib_module {
    ...
};
```

## Topics

### Instance Properties
- [iextdefsym](dylib_module/1525753-iextdefsym.md)
- [iextrel](dylib_module/1525367-iextrel.md)
  The index into the external relocation table of the first entry provided by this module.
- [iinit_iterm](dylib_module/1525500-iinit_iterm.md)
- [ilocalsym](dylib_module/1525836-ilocalsym.md)
- [irefsym](dylib_module/1525535-irefsym.md)
- [module_name](dylib_module/1525720-module_name.md)
- [nextdefsym](dylib_module/1525847-nextdefsym.md)
- [nextrel](dylib_module/1525709-nextrel.md)
- [ninit_nterm](dylib_module/1525476-ninit_nterm.md)
  Contains both the number of pointers in the module initialization (the low 16 bits) and the number of pointers in the module termination section (the high 16 bits) for this module.
- [nlocalsym](dylib_module/1525881-nlocalsym.md)
- [nrefsym](dylib_module/1525667-nrefsym.md)
  The number of external reference entries provided by this module.
- [objc_module_info_addr](dylib_module/1525527-objc_module_info_addr.md)
- [objc_module_info_size](dylib_module/1525353-objc_module_info_size.md)

## See Also

- [dyld_info_command](dyld_info_command.md)
- [dyld_kernel_image_info_array_t](dyld_kernel_image_info_array_t.md)
- [dyld_uuid_info_32](dyld_uuid_info_32.md)
- [dyld_uuid_info_64](dyld_uuid_info_64.md)
- [dyld_uuid_info_64_v2](dyld_uuid_info_64_v2.md)
- [dylib](dylib.md)
- [dylib_command](dylib_command.md)
- [dylib_module_64](dylib_module_64.md)
- [dylib_reference](dylib_reference.md)
- [dylib_table_of_contents](dylib_table_of_contents.md)
- [dylinker_command](dylinker_command.md)
- [dysymtab_command](dysymtab_command.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/dylib_module)*