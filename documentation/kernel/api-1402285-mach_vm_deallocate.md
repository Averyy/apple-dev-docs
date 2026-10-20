# mach_vm_deallocate

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
kern_return_t mach_vm_deallocate(vm_map_t target, mach_vm_address_t address, mach_vm_size_t size);
```

## See Also

### Creation and Destruction
- [mach_vm_allocate](./api-1402376-mach_vm_allocate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402285-mach_vm_deallocate)*