# mach_vm_region_info_64

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t mach_vm_region_info_64(vm_map_read_t task, vm_address_t address, vm_info_region_64_t *region, vm_info_object_array_t *objects, mach_msg_type_number_t *objectsCnt);
```

## See Also

- [mach_vm_region](1402149-mach_vm_region.md)
- [mach_vm_region_info](1585270-mach_vm_region_info.md)
- [mach_vm_region_recurse](1402114-mach_vm_region_recurse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585170-mach_vm_region_info_64)*