# vfs_attr_pack_ext

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.15+

## Declaration

```swift
errno_t vfs_attr_pack_ext(mount_t mp, vnode_t vp, uio_t uio, struct attrlist *alp, uint64_t options, struct vnode_attr *vap, void *fndesc, vfs_context_t ctx);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3353091-vfs_attr_pack_ext)*