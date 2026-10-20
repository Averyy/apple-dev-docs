# vm_read_overwrite

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t vm_read_overwrite(vm_map_read_t target_task, vm_address_t address, vm_size_t size, vm_address_t data, vm_size_t *outsize);
```

## See Also

- [vm_read](1585350-vm_read.md)
- [vm_read_list](1585516-vm_read_list.md)
- [vm_write](1585462-vm_write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585371-vm_read_overwrite)*