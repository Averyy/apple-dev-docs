# vfs_quotactl

**Framework**: Kernel  
**Kind**: structp

**Availability**:
- macOS 10.6+

## Declaration

```swift
int (*vfs_quotactl)(struct mount *mp, int cmds, uid_t uid, caddr_t arg, vfs_context_t context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vfsops/1523271-vfs_quotactl)*