# vm_wire

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t vm_wire(host_priv_t host_priv, vm_map_t task, vm_address_t address, vm_size_t size, vm_prot_t desired_access);
```

## See Also

### Configuration
- [vm_protect](./api-1585294-vm_protect.md)
- [mach_memory_info](./api-1502832-mach_memory_info.md)
- [vm_behavior_set](./api-1585236-vm_behavior_set.md)
- [vm_machine_attribute](./api-1585354-vm_machine_attribute.md)
- [vm_purgable_control](./api-1585267-vm_purgable_control.md)
- [vm_inherit](./api-1585275-vm_inherit.md)
- [vm_msync](./api-1585201-vm_msync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1588985-vm_wire)*