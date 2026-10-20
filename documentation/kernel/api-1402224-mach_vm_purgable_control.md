# mach_vm_purgable_control

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```c
kern_return_t mach_vm_purgable_control(vm_map_t target_task, mach_vm_address_t address, vm_purgable_t control, int *state);
```

## See Also

### Configuration
- [mach_vm_protect](./api-1402291-mach_vm_protect.md)
- [mach_vm_wire](./api-1588962-mach_vm_wire.md)
- [mach_vm_inherit](./api-1402141-mach_vm_inherit.md)
- [mach_vm_machine_attribute](./api-1402429-mach_vm_machine_attribute.md)
- [mach_vm_msync](./api-1402328-mach_vm_msync.md)
- [mach_vm_behavior_set](./api-1402468-mach_vm_behavior_set.md)
- [mach_vm_page_info](./api-1402504-mach_vm_page_info.md)
- [mach_vm_page_query](./api-1402261-mach_vm_page_query.md)
- [mach_vm_page_range_query](./api-2890784-mach_vm_page_range_query.md)
- [mach_vm_round_page_overflow](./api-1643689-mach_vm_round_page_overflow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402224-mach_vm_purgable_control)*