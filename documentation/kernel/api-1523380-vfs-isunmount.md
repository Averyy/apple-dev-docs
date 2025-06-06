# vfs_isunmount

**Framework**: Kernel  
**Kind**: func

Determine if an unmount is in progress.

**Availability**:
- macOS 10.6+

## Declaration

```swift
int vfs_isunmount(mount_t mp);
```

#### Return_value

Nonzero if an unmount is in progress, else zero.

#### Discussion

This is an unsynchronized snapshot of the mount state. It should only be called if the mount is known to be valid, e.g. there are known to be live files on that volume.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523380-vfs_isunmount)*