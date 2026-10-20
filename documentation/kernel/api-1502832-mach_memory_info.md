# mach_memory_info

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.11+

## Declaration

```c
kern_return_t mach_memory_info(mach_port_t host, mach_zone_name_array_t *names, mach_msg_type_number_t *namesCnt, mach_zone_info_array_t *info, mach_msg_type_number_t *infoCnt, mach_memory_info_array_t *memory_info, mach_msg_type_number_t *memory_infoCnt);
```

## See Also

### Configuration
- [vm_protect](./api-1585294-vm_protect.md)
- [vm_wire](./api-1588985-vm_wire.md)
- [vm_behavior_set](./api-1585236-vm_behavior_set.md)
- [vm_machine_attribute](./api-1585354-vm_machine_attribute.md)
- [vm_purgable_control](./api-1585267-vm_purgable_control.md)
- [vm_inherit](./api-1585275-vm_inherit.md)
- [vm_msync](./api-1585201-vm_msync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1502832-mach_memory_info)*