# sysctl_handle_int

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
int sysctl_handle_int(struct sysctl_oid *oidp, void *arg1, int arg2, struct sysctl_req *req);
```

## See Also

- [sysctl_handle_int2quad](1404249-sysctl_handle_int2quad.md)
- [sysctl_handle_long](1404379-sysctl_handle_long.md)
- [sysctl_handle_opaque](1404289-sysctl_handle_opaque.md)
- [sysctl_handle_quad](1404243-sysctl_handle_quad.md)
- [sysctl_handle_string](1404297-sysctl_handle_string.md)
- [sysctl_io_number](1404223-sysctl_io_number.md)
- [sysctl_io_opaque](1404235-sysctl_io_opaque.md)
- [sysctl_io_string](1404325-sysctl_io_string.md)
- [sysctl_register_oid](1404241-sysctl_register_oid.md)
- [sysctl_unregister_oid](1404403-sysctl_unregister_oid.md)
- [sysctlbyname](1387446-sysctlbyname.md)
  Gets or sets information about the system and environment.
- [sysctl__children](sysctl_children.md)
- [sysctl__debug_children](sysctl_debug_children.md)
- [sysctl__hw_children](sysctl_hw_children.md)
- [sysctl__kern_children](sysctl_kern_children.md)
- [sysctl__machdep_children](sysctl_machdep_children.md)
- [sysctl__net_children](sysctl_net_children.md)
- [sysctl__sysctl_children](sysctl_sysctl_children.md)
- [sysctl__user_children](sysctl_user_children.md)
- [sysctl__vfs_children](sysctl_vfs_children.md)
- [sysctl__vm_children](sysctl_vm_children.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1404317-sysctl_handle_int)*