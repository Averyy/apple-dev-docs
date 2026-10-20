# vfs_setlocklocal

**Framework**: Kernel  
**Kind**: func

Mark a filesystem as using VFS-level advisory locking support.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_setlocklocal(mount_t mp);
```

#### Return_value

void.

#### Discussion

Advisory locking operations will not call down to the filesystem if this flag is set.

## Parameters

- `mp`: Mount to mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523104-vfs_setlocklocal)*