# receive_vfs_resolve_file

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
kern_return_t receive_vfs_resolve_file(mach_port_t nspace_handler_port, uint32_t req_id, uint32_t pid, uint32_t op, int64_t offset, int64_t size, nspace_path_t path);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3753683-receive_vfs_resolve_file)*