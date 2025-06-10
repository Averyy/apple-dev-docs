# vfs_ioctl

**Framework**: Kernel  
**Kind**: structp

**Availability**:
- macOS 10.12+

## Declaration

```swift
int (*vfs_ioctl)(struct mount *mp, u_long command, caddr_t data, int flags, vfs_context_t context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vfsops/1646282-vfs_ioctl)*