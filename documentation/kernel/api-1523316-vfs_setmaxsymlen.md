# vfs_setmaxsymlen

**Framework**: Kernel  
**Kind**: func

Set the maximum length of a symbolic link on a filesystem.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_setmaxsymlen(mount_t mp, uint32_t symlen);
```

#### Return_value

Max symlink length.

## Parameters

- `mp`: Mount on which to set symlink length cap.
- `symlen`: Length to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523316-vfs_setmaxsymlen)*