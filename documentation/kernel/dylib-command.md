# dylib_command

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct dylib_command {
    ...
};
```

## Topics

### Instance Properties
- [cmd](dylib_command/1525289-cmd.md)
  Common to all load command structures. For this structure, set to either `LC_LOAD_DYLIB`, `LC_LOAD_WEAK_DYLIB`, or `LC_ID_DYLIB`.
- [cmdsize](dylib_command/1525270-cmdsize.md)
- [dylib](dylib_command/1525891-dylib.md)

## See Also

- [dyld_info_command](dyld_info_command.md)
- [dyld_kernel_image_info_array_t](dyld_kernel_image_info_array_t.md)
- [dyld_uuid_info_32](dyld_uuid_info_32.md)
- [dyld_uuid_info_64](dyld_uuid_info_64.md)
- [dyld_uuid_info_64_v2](dyld_uuid_info_64_v2.md)
- [dylib](dylib.md)
- [dylib_module](dylib_module.md)
- [dylib_module_64](dylib_module_64.md)
- [dylib_reference](dylib_reference.md)
- [dylib_table_of_contents](dylib_table_of_contents.md)
- [dylinker_command](dylinker_command.md)
- [dysymtab_command](dysymtab_command.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/dylib_command)*