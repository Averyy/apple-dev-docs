# vm_allocate

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t vm_allocate(vm_map_t target_task, vm_address_t *address, vm_size_t size, int flags);
```

## See Also

### Creation and Destruction
- [vm_allocate_cpm](./api-1588863-vm_allocate_cpm.md)
- [vm_deallocate](./api-1585284-vm_deallocate.md)
- [vm_copy](./api-1585277-vm_copy.md)
- [mach_vm_copy](./api-1402342-mach_vm_copy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585381-vm_allocate)*