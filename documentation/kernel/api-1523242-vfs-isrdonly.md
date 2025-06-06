# vfs_isrdonly

**Framework**: Kernel  
**Kind**: func

Determine if a filesystem is mounted read-only.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_isrdonly(mount_t mp);
```

#### Return_value

Nonzero if filesystem is mounted read-only, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523242-vfs_isrdonly)*