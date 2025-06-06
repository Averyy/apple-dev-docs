# vfs_getvfs

**Framework**: Kernel  
**Kind**: func

Given a filesystem ID, look up a mount structure.

**Availability**:
- macOS 10.4+

## Declaration

```swift
mount_t vfs_getvfs(fsid_t *fsid);
```

#### Return_value

Mountpoint if found, else NULL. Note unmounting mountpoints can be returned.

## Parameters

- `fsid`: Filesystem ID to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523465-vfs_getvfs)*