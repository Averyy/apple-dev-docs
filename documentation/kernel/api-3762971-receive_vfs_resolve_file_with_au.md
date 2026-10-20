# receive_vfs_resolve_file_with_audit_token

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
kern_return_t receive_vfs_resolve_file_with_audit_token(mach_port_t nspace_handler_port, uint32_t req_id, uint32_t op, int64_t offset, int64_t size, nspace_path_t path, audit_token_t req_atoken, audit_token_t atoken);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3762971-receive_vfs_resolve_file_with_au)*