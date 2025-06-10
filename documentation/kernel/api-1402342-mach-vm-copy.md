# mach_vm_copy

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
kern_return_t mach_vm_copy(vm_map_t target_task, mach_vm_address_t source_address, mach_vm_size_t size, mach_vm_address_t dest_address);
```

## See Also

- [vm_allocate](1585381-vm_allocate.md)
- [vm_allocate_cpm](1588863-vm_allocate_cpm.md)
- [vm_deallocate](1585284-vm_deallocate.md)
- [vm_copy](1585277-vm_copy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402342-mach_vm_copy)*