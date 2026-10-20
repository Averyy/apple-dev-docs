# vfs_mount

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- macOS 10.6+

## Declaration

```c
int (*vfs_mount)(struct mount *mp, vnode_t devvp, user_addr_t data, vfs_context_t context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vfsops/1523530-vfs_mount)*