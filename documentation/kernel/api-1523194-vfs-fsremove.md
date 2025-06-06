# vfs_fsremove

**Framework**: Kernel  
**Kind**: func

Unregister a filesystem with VFS.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_fsremove(vfstable_t handle);
```

#### Return_value

0 for success, else an error code.

#### Discussion

Typically called by a filesystem Kernel Extension when it is unloaded.

## Parameters

- `handle`: Handle which was returned by vfs_fsadd.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523194-vfs_fsremove)*