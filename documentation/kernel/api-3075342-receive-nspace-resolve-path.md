# receive_nspace_resolve_path

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.15+

## Declaration

```swift
kern_return_t receive_nspace_resolve_path(mach_port_t nspace_handler_port, uint32_t req_id, uint32_t pid, uint32_t op, nspace_path_t path, int *resolve_error);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3075342-receive_nspace_resolve_path)*