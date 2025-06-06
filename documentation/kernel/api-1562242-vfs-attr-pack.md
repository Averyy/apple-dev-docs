# vfs_attr_pack

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.10+

## Declaration

```swift
errno_t vfs_attr_pack(vnode_t vp, uio_t uio, struct attrlist *alp, uint64_t options, struct vnode_attr *vap, void *fndesc, vfs_context_t ctx);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562242-vfs_attr_pack)*