# vfs_setlocklocal

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Mark a filesystem as using VFS-level advisory locking support.

**Availability**:
- macOS 10.4+

## Declaration

```c
void vfs_setlocklocal(mount_t mp);
```

#### Return Value

void.

#### Discussion

Advisory locking operations will not call down to the filesystem if this flag is set.

## Parameters

- `mp`: Mount to mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523104-vfs_setlocklocal)*