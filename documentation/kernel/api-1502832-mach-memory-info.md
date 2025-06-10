# mach_memory_info

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.11+

## Declaration

```swift
kern_return_t mach_memory_info(mach_port_t host, mach_zone_name_array_t *names, mach_msg_type_number_t *namesCnt, mach_zone_info_array_t *info, mach_msg_type_number_t *infoCnt, mach_memory_info_array_t *memory_info, mach_msg_type_number_t *memory_infoCnt);
```

## See Also

- [vm_protect](1585294-vm_protect.md)
- [vm_wire](1588985-vm_wire.md)
- [vm_behavior_set](1585236-vm_behavior_set.md)
- [vm_machine_attribute](1585354-vm_machine_attribute.md)
- [vm_purgable_control](1585267-vm_purgable_control.md)
- [vm_inherit](1585275-vm_inherit.md)
- [vm_msync](1585201-vm_msync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1502832-mach_memory_info)*