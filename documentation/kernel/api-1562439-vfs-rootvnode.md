# vfs_rootvnode

**Framework**: Kernel  
**Kind**: func

Returns the root vnode with an iocount.

**Availability**:
- macOS 10.5+

## Declaration

```swift
vnode_t vfs_rootvnode(void);
```

#### Return_value

Pointer to root vnode if successful; error code if there is a problem taking an iocount.

#### Discussion

Caller must vnode_put() the root node when done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562439-vfs_rootvnode)*