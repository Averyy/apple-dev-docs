# mach_vm_read_list

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
kern_return_t mach_vm_read_list(vm_map_read_t target_task, mach_vm_read_entry_t data_list, natural_t count);
```

## See Also

### Reads and Writes
- [mach_vm_read](./api-1402405-mach_vm_read.md)
- [mach_vm_write](./api-1402070-mach_vm_write.md)
- [mach_vm_read_overwrite](./api-1402127-mach_vm_read_overwrite.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402084-mach_vm_read_list)*