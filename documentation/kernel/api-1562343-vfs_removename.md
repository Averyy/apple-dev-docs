# vfs_removename

**Framework**: Kernel  
**Kind**: func

Deprecated

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_removename(const char *name);
```

#### Discussion

vnode_update_identity() and vnode_create() make vfs_addname() unnecessary for kexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562343-vfs_removename)*