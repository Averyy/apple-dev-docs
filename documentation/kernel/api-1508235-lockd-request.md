# lockd_request

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.5+

## Declaration

```swift
kern_return_t lockd_request(mach_port_t server, uint32_t vers, uint32_t flags, uint64_t xid, int64_t flk_start, int64_t flk_len, int32_t flk_pid, int32_t flk_type, int32_t flk_whence, sock_storage sock_address, xcred cred, uint32_t fh_len, nfs_handle fh);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1508235-lockd_request)*