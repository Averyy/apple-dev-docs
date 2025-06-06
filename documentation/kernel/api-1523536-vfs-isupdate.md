# vfs_isupdate

**Framework**: Kernel  
**Kind**: func

Determine if a mount update is in progress.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_isupdate(mount_t mp);
```

#### Return_value

Nonzero if a mount update is in progress, 0 otherwise.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523536-vfs_isupdate)*