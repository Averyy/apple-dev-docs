# doubleagent_allocate_xattr

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 15.0+

## Declaration

```swift
kern_return_t doubleagent_allocate_xattr(mach_port_t server, mach_port_t file_port, int64_t file_size, xattrname name, uint64_t size, uint32_t options, int *err, uint64_t *value_offset);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4359982-doubleagent_allocate_xattr)*