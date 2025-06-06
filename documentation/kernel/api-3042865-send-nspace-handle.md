# send_nspace_handle

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.15+

## Declaration

```swift
kern_return_t send_nspace_handle(mach_port_t nspace_handler_port, uint32_t pid, vfs_path_t path, int *handler_error);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3042865-send_nspace_handle)*