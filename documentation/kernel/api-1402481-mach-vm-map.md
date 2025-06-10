# mach_vm_map

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
kern_return_t mach_vm_map(vm_map_t target_task, mach_vm_address_t *address, mach_vm_size_t size, mach_vm_offset_t mask, int flags, mem_entry_name_port_t object, memory_object_offset_t offset, boolean_t copy, vm_prot_t cur_protection, vm_prot_t max_protection, vm_inherit_t inheritance);
```

## See Also

- [mach_vm_remap](1402218-mach_vm_remap.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402481-mach_vm_map)*