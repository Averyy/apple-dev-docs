# vm_protect

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t vm_protect(vm_map_t target_task, vm_address_t address, vm_size_t size, boolean_t set_maximum, vm_prot_t new_protection);
```

## See Also

- [vm_wire](1588985-vm_wire.md)
- [mach_memory_info](1502832-mach_memory_info.md)
- [vm_behavior_set](1585236-vm_behavior_set.md)
- [vm_machine_attribute](1585354-vm_machine_attribute.md)
- [vm_purgable_control](1585267-vm_purgable_control.md)
- [vm_inherit](1585275-vm_inherit.md)
- [vm_msync](1585201-vm_msync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585294-vm_protect)*