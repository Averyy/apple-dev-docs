# mach_vm_page_info

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.6+

## Declaration

```swift
kern_return_t mach_vm_page_info(vm_map_read_t target_task, mach_vm_address_t address, vm_page_info_flavor_t flavor, vm_page_info_t info, mach_msg_type_number_t *infoCnt);
```

## See Also

- [mach_vm_protect](1402291-mach_vm_protect.md)
- [mach_vm_wire](1588962-mach_vm_wire.md)
- [mach_vm_inherit](1402141-mach_vm_inherit.md)
- [mach_vm_machine_attribute](1402429-mach_vm_machine_attribute.md)
- [mach_vm_msync](1402328-mach_vm_msync.md)
- [mach_vm_purgable_control](1402224-mach_vm_purgable_control.md)
- [mach_vm_behavior_set](1402468-mach_vm_behavior_set.md)
- [mach_vm_page_query](1402261-mach_vm_page_query.md)
- [mach_vm_page_range_query](2890784-mach_vm_page_range_query.md)
- [mach_vm_round_page_overflow](1643689-mach_vm_round_page_overflow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402504-mach_vm_page_info)*