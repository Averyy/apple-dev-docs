# doubleagent_lookup_xattr

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 15.0+

## Declaration

```swift
kern_return_t doubleagent_lookup_xattr(mach_port_t server, mach_port_t file_port, int64_t file_size, xattrname name, int *err, uint64_t *value_offset, uint64_t *value_length);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4359984-doubleagent_lookup_xattr)*