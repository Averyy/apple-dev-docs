# vfs_isrdwr

**Framework**: Kernel  
**Kind**: func

Determine if a filesystem is mounted with writes enabled.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_isrdwr(mount_t mp);
```

#### Return_value

Nonzero if filesystem is mounted read-write, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523454-vfs_isrdwr)*