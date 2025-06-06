# dysymtab_command

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct dysymtab_command {
    ...
};
```

## Topics

### Instance Properties
- [cmd](dysymtab_command/1525903-cmd.md)
  Common to all load command structures. For this structure, set to `LC_DYSYMTAB`.
- [cmdsize](dysymtab_command/1525635-cmdsize.md)
- [extrefsymoff](dysymtab_command/1525833-extrefsymoff.md)
  An integer indicating the byte offset from the start of the file to the external reference table data.
- [extreloff](dysymtab_command/1525933-extreloff.md)
  An integer indicating the byte offset from the start of the file to the external relocation table data.
- [iextdefsym](dysymtab_command/1525498-iextdefsym.md)
- [ilocalsym](dysymtab_command/1525772-ilocalsym.md)
- [indirectsymoff](dysymtab_command/1525396-indirectsymoff.md)
- [iundefsym](dysymtab_command/1525248-iundefsym.md)
- [locreloff](dysymtab_command/1525752-locreloff.md)
- [modtaboff](dysymtab_command/1525815-modtaboff.md)
- [nextdefsym](dysymtab_command/1525390-nextdefsym.md)
- [nextrefsyms](dysymtab_command/1525576-nextrefsyms.md)
- [nextrel](dysymtab_command/1525818-nextrel.md)
- [nindirectsyms](dysymtab_command/1525507-nindirectsyms.md)
- [nlocalsym](dysymtab_command/1525269-nlocalsym.md)
- [nlocrel](dysymtab_command/1525762-nlocrel.md)
- [nmodtab](dysymtab_command/1525921-nmodtab.md)
- [ntoc](dysymtab_command/1525405-ntoc.md)
- [nundefsym](dysymtab_command/1525375-nundefsym.md)
- [tocoff](dysymtab_command/1525597-tocoff.md)

## See Also

- [dyld_info_command](dyld_info_command.md)
- [dyld_kernel_image_info_array_t](dyld_kernel_image_info_array_t.md)
- [dyld_uuid_info_32](dyld_uuid_info_32.md)
- [dyld_uuid_info_64](dyld_uuid_info_64.md)
- [dyld_uuid_info_64_v2](dyld_uuid_info_64_v2.md)
- [dylib](dylib.md)
- [dylib_command](dylib_command.md)
- [dylib_module](dylib_module.md)
- [dylib_module_64](dylib_module_64.md)
- [dylib_reference](dylib_reference.md)
- [dylib_table_of_contents](dylib_table_of_contents.md)
- [dylinker_command](dylinker_command.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/dysymtab_command)*