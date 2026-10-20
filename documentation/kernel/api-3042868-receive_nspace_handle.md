# receive_nspace_handle

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.15+

## Declaration

```c
kern_return_t receive_nspace_handle(mach_port_t nspace_handler_port, uint32_t pid, vfs_path_t path, int *handler_error);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3042868-receive_nspace_handle)*