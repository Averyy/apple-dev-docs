# mach_vm_page_query

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
kern_return_t mach_vm_page_query(vm_map_read_t target_map, mach_vm_offset_t offset, integer_t *disposition, integer_t *ref_count);
```

## See Also

### Configuration
- [mach_vm_protect](./api-1402291-mach_vm_protect.md)
- [mach_vm_wire](./api-1588962-mach_vm_wire.md)
- [mach_vm_inherit](./api-1402141-mach_vm_inherit.md)
- [mach_vm_machine_attribute](./api-1402429-mach_vm_machine_attribute.md)
- [mach_vm_msync](./api-1402328-mach_vm_msync.md)
- [mach_vm_purgable_control](./api-1402224-mach_vm_purgable_control.md)
- [mach_vm_behavior_set](./api-1402468-mach_vm_behavior_set.md)
- [mach_vm_page_info](./api-1402504-mach_vm_page_info.md)
- [mach_vm_page_range_query](./api-2890784-mach_vm_page_range_query.md)
- [mach_vm_round_page_overflow](./api-1643689-mach_vm_round_page_overflow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402261-mach_vm_page_query)*