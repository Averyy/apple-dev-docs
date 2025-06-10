# vfs_mount

**Framework**: Kernel  
**Kind**: structp

**Availability**:
- macOS 10.6+

## Declaration

```swift
int (*vfs_mount)(struct mount *mp, vnode_t devvp, user_addr_t data, vfs_context_t context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vfsops/1523530-vfs_mount)*