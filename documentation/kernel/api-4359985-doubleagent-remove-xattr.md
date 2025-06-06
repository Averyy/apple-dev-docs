# doubleagent_remove_xattr

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 15.0+

## Declaration

```swift
kern_return_t doubleagent_remove_xattr(mach_port_t server, mach_port_t file_port, int64_t file_size, xattrname name, int *err, boolean_t *is_empty);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4359985-doubleagent_remove_xattr)*