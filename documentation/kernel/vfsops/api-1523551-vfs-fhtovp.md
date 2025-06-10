# vfs_fhtovp

**Framework**: Kernel  
**Kind**: structp

**Availability**:
- macOS 10.6+

## Declaration

```swift
int (*vfs_fhtovp)(struct mount *mp, int fhlen, unsigned char *fhp, struct vnode **vpp, vfs_context_t context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vfsops/1523551-vfs_fhtovp)*