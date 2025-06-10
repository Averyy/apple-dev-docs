# mach_vm_write

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
kern_return_t mach_vm_write(vm_map_t target_task, mach_vm_address_t address, vm_offset_t data, mach_msg_type_number_t dataCnt);
```

## See Also

- [mach_vm_read](1402405-mach_vm_read.md)
- [mach_vm_read_list](1402084-mach_vm_read_list.md)
- [mach_vm_read_overwrite](1402127-mach_vm_read_overwrite.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402070-mach_vm_write)*