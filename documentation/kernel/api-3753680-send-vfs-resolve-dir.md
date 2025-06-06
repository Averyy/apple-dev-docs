# send_vfs_resolve_dir

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
kern_return_t send_vfs_resolve_dir(mach_port_t nspace_handler_port, uint32_t req_id, uint32_t pid, uint32_t op, nspace_name_t file_name, nspace_path_t path);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3753680-send_vfs_resolve_dir)*