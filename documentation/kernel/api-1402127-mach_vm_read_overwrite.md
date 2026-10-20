# mach_vm_read_overwrite

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
kern_return_t mach_vm_read_overwrite(vm_map_read_t target_task, mach_vm_address_t address, mach_vm_size_t size, mach_vm_address_t data, mach_vm_size_t *outsize);
```

## See Also

### Reads and Writes
- [mach_vm_read](./api-1402405-mach_vm_read.md)
- [mach_vm_write](./api-1402070-mach_vm_write.md)
- [mach_vm_read_list](./api-1402084-mach_vm_read_list.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402127-mach_vm_read_overwrite)*