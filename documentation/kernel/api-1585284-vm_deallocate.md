# vm_deallocate

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t vm_deallocate(vm_map_t target_task, vm_address_t address, vm_size_t size);
```

## See Also

### Creation and Destruction
- [vm_allocate](./api-1585381-vm_allocate.md)
- [vm_allocate_cpm](./api-1588863-vm_allocate_cpm.md)
- [vm_copy](./api-1585277-vm_copy.md)
- [mach_vm_copy](./api-1402342-mach_vm_copy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585284-vm_deallocate)*