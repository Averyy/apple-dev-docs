# vm_allocate_cpm

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t vm_allocate_cpm(host_priv_t host_priv, vm_map_t task, vm_address_t *address, vm_size_t size, int flags);
```

## See Also

- [vm_allocate](1585381-vm_allocate.md)
- [vm_deallocate](1585284-vm_deallocate.md)
- [vm_copy](1585277-vm_copy.md)
- [mach_vm_copy](1402342-mach_vm_copy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1588863-vm_allocate_cpm)*