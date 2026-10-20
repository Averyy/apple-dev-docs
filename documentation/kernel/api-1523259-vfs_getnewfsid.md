# vfs_getnewfsid

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Generate a unique filesystem ID for a mount and store it in the mount structure.

**Availability**:
- macOS 10.4+

## Declaration

```c
void vfs_getnewfsid(struct mount *mp);
```

#### Return Value

void.

#### Discussion

Filesystem IDs are returned as part of "struct statfs." This function is typically called as part of file-system specific mount code (i.e. through VFS_MOUNT).

## Parameters

- `mp`: Mount to set an ID for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523259-vfs_getnewfsid)*