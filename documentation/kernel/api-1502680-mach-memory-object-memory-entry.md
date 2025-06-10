# mach_memory_object_memory_entry

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t mach_memory_object_memory_entry(host_t host, boolean_t internal, vm_size_t size, vm_prot_t permission, memory_object_t pager, mach_port_t *entry_handle);
```

## See Also

- [mach_memory_object_memory_entry_64](1502560-mach_memory_object_memory_entry_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1502680-mach_memory_object_memory_entry)*