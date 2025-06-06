# vfs_maxsymlen

**Framework**: Kernel  
**Kind**: func

Get the maximum length of a symbolic link on a filesystem.

**Availability**:
- macOS 10.4+

## Declaration

```swift
uint32_t vfs_maxsymlen(mount_t mp);
```

#### Return_value

Max symlink length.

## Parameters

- `mp`: Mount from which to get symlink length cap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523507-vfs_maxsymlen)*