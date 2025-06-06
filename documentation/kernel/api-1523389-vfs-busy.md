# vfs_busy

**Framework**: Kernel  
**Kind**: func

"Busy" a mountpoint.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_busy(mount_t mp, int flags);
```

#### Return_value

0 for success, with a lock held; an error code otherwise, with no lock held.

#### Discussion

vfs_busy() will "busy" a mountpoint, preventing unmounts from taking off, by taking its reader-writer lock in a shared manner. If a mount is dead, it will fail; if an unmount is in progress, depending on flags, it will either fail immediately or block until the unmount completes (then failing if the unmount has succeeded, or potentially succeeding if unmounting failed). A successful vfs_busy() must be followed by a vfs_unbusy() to release the lock on the mount.

## Parameters

- `mp`: Mount to busy.
- `flags`: LK_NOWAIT: fail with ENOENT if an unmount is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523389-vfs_busy)*