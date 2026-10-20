# mach_vm_copy

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
kern_return_t mach_vm_copy(vm_map_t target_task, mach_vm_address_t source_address, mach_vm_size_t size, mach_vm_address_t dest_address);
```

## See Also

### Creation and Destruction
- [vm_allocate](./api-1585381-vm_allocate.md)
- [vm_allocate_cpm](./api-1588863-vm_allocate_cpm.md)
- [vm_deallocate](./api-1585284-vm_deallocate.md)
- [vm_copy](./api-1585277-vm_copy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402342-mach_vm_copy)*