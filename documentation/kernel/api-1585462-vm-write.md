# vm_write

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t vm_write(vm_map_t target_task, vm_address_t address, vm_offset_t data, mach_msg_type_number_t dataCnt);
```

## See Also

- [vm_read](1585350-vm_read.md)
- [vm_read_list](1585516-vm_read_list.md)
- [vm_read_overwrite](1585371-vm_read_overwrite.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585462-vm_write)*