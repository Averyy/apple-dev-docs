# mach_vm_read_overwrite

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
kern_return_t mach_vm_read_overwrite(vm_map_read_t target_task, mach_vm_address_t address, mach_vm_size_t size, mach_vm_address_t data, mach_vm_size_t *outsize);
```

## See Also

- [mach_vm_read](1402405-mach_vm_read.md)
- [mach_vm_write](1402070-mach_vm_write.md)
- [mach_vm_read_list](1402084-mach_vm_read_list.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402127-mach_vm_read_overwrite)*