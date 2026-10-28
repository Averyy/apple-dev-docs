# vfs_getvfs

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Given a filesystem ID, look up a mount structure.

**Availability**:
- macOS 10.4+

## Declaration

```c
mount_t vfs_getvfs(fsid_t *fsid);
```

## Return Value

Mountpoint if found, else NULL. Note unmounting mountpoints can be returned.

## Parameters

- `fsid`: Filesystem ID to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523465-vfs_getvfs)*