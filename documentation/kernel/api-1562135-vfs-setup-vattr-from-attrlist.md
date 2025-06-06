# vfs_setup_vattr_from_attrlist

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.10+

## Declaration

```swift
errno_t vfs_setup_vattr_from_attrlist(struct attrlist *alp, struct vnode_attr *vap, enum vtype obj_vtype, ssize_t *attr_fixed_sizep, vfs_context_t ctx);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562135-vfs_setup_vattr_from_attrlist)*