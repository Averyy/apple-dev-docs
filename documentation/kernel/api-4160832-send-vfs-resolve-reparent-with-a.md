# send_vfs_resolve_reparent_with_audit_token

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 14.0+

## Declaration

```swift
kern_return_t send_vfs_resolve_reparent_with_audit_token(mach_port_t nspace_handler_port, uint32_t req_id, uint32_t op, nspace_path_t path, nspace_path_t dest_path, audit_token_t req_atoken);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4160832-send_vfs_resolve_reparent_with_a)*