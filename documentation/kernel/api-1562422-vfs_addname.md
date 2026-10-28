# vfs_addname

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Deprecated

**Availability**:
- macOS 10.4+

## Declaration

```c
const char * vfs_addname(const char *name, uint32_t len, uint32_t nc_hash, uint32_t flags);
```

## Discussion

vnode_update_identity() and vnode_create() make vfs_addname() unnecessary for kexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562422-vfs_addname)*