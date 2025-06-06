# vfs_unbusy

**Framework**: Kernel  
**Kind**: func

"Unbusy" a mountpoint by releasing its read-write lock.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_unbusy(mount_t mp);
```

#### Return_value

void.

#### Discussion

A successful vfs_busy() must be followed by a vfs_unbusy() to release the lock on the mount.

## Parameters

- `mp`: Mount to unbusy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523451-vfs_unbusy)*