# vfs_vget

**Framework**: Kernel  
**Kind**: structp

**Availability**:
- macOS 10.6+

## Declaration

```swift
int (*vfs_vget)(struct mount *mp, ino64_t ino, struct vnode **vpp, vfs_context_t context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vfsops/1523430-vfs_vget)*