# vn_revoke

**Framework**: Kernel  
**Kind**: func

Invalidate all references to a vnode.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vn_revoke(vnode_t vp, int flags, vfs_context_t ctx);
```

#### Return_value

0 always.

#### Discussion

Reclaims the vnode, giving it deadfs vnops (though not halting operations which are already in progress). Also reclaims all aliased vnodes (important for devices). People holding usecounts on the vnode, e.g. processes with the file open, will find that all subsequent operations but closing the file fail.

## Parameters

- `vp`: The vnode to revoke.
- `flags`: Unused.
- `ctx`: Context against which to validate operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562348-vn_revoke)*