# send_vfs_resolve_dir_with_audit_token

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
kern_return_t send_vfs_resolve_dir_with_audit_token(mach_port_t nspace_handler_port, uint32_t req_id, uint32_t op, nspace_name_t file_name, nspace_path_t path, audit_token_t req_atoken);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3762968-send_vfs_resolve_dir_with_audit_)*