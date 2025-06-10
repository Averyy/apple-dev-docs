# a_dir_clone_authorizer

**Framework**: Kernel  
**Kind**: structp

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
int (*a_dir_clone_authorizer)(struct vnode_attr *vap, kauth_action_t action, struct vnode_attr *dvap, vnode_t sdvp, mount_t mp, dir_clone_authorizer_op_t vattr_op, uint32_t flags, vfs_context_t ctx, void *reserved);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vnop_clonefile_args/2818591-a_dir_clone_authorizer)*