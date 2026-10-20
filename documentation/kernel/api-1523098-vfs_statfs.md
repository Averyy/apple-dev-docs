# vfs_statfs

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Get information about filesystem status.

**Availability**:
- macOS 10.4+

## Declaration

```c
struct vfsstatfs * vfs_statfs(mount_t mp);
```

#### Return Value

Pointer to vfsstatfs.

#### Discussion

Each filesystem has a struct vfsstatfs associated with it which is updated as events occur; this function returns a pointer to it. Note that the data in the structure will continue to change over time and also that it may be quite stale of vfs_update_vfsstat has not been called recently.

## Parameters

- `mp`: Mount for which to get vfsstatfs pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523098-vfs_statfs)*