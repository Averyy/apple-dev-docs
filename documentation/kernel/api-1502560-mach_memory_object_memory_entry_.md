# mach_memory_object_memory_entry_64

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t mach_memory_object_memory_entry_64(host_t host, boolean_t internal, memory_object_size_t size, vm_prot_t permission, memory_object_t pager, mach_port_t *entry_handle);
```

## See Also

### Memory Objects
- [mach_memory_object_memory_entry](./api-1502680-mach_memory_object_memory_entry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1502560-mach_memory_object_memory_entry_)*