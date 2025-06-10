# vm_msync

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t vm_msync(vm_map_t target_task, vm_address_t address, vm_size_t size, vm_sync_t sync_flags);
```

## See Also

- [vm_protect](1585294-vm_protect.md)
- [vm_wire](1588985-vm_wire.md)
- [mach_memory_info](1502832-mach_memory_info.md)
- [vm_behavior_set](1585236-vm_behavior_set.md)
- [vm_machine_attribute](1585354-vm_machine_attribute.md)
- [vm_purgable_control](1585267-vm_purgable_control.md)
- [vm_inherit](1585275-vm_inherit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585201-vm_msync)*