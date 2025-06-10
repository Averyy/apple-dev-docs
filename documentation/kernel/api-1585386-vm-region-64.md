# vm_region_64

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t vm_region_64(vm_map_read_t target_task, vm_address_t *address, vm_size_t *size, vm_region_flavor_t flavor, vm_region_info_t info, mach_msg_type_number_t *infoCnt, mach_port_t *object_name);
```

## See Also

- [vm_region](1585377-vm_region.md)
- [vm_region_recurse](1585351-vm_region_recurse.md)
- [vm_region_recurse_64](1585424-vm_region_recurse_64.md)
- [vm_region_basic_info_data_64_t](vm_region_basic_info_data_64_t.md)
- [vm_region_basic_info_data_t](vm_region_basic_info_data_t.md)
- [vm_region_extended_info_data_t](vm_region_extended_info_data_t.md)
- [vm_region_submap_info_data_64_t](vm_region_submap_info_data_64_t.md)
- [vm_region_submap_info_data_t](vm_region_submap_info_data_t.md)
- [vm_region_submap_short_info_data_64_t](vm_region_submap_short_info_data_64_t.md)
- [vm_region_top_info_data_t](vm_region_top_info_data_t.md)
- [vm_page_info_basic_data_t](vm_page_info_basic_data_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585386-vm_region_64)*