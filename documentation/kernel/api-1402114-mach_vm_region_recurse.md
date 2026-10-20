# mach_vm_region_recurse

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
kern_return_t mach_vm_region_recurse(vm_map_read_t target_task, mach_vm_address_t *address, mach_vm_size_t *size, natural_t *nesting_depth, vm_region_recurse_info_t info, mach_msg_type_number_t *infoCnt);
```

## See Also

### Regions
- [mach_vm_region](./api-1402149-mach_vm_region.md)
- [mach_vm_region_info](./api-1585270-mach_vm_region_info.md)
- [mach_vm_region_info_64](./api-1585170-mach_vm_region_info_64.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402114-mach_vm_region_recurse)*