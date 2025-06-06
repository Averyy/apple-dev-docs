# vfs_issynchronous

**Framework**: Kernel  
**Kind**: func

Determine if writes to a filesystem occur synchronously.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_issynchronous(mount_t mp);
```

#### Return_value

Nonzero if writes occur synchronously, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523327-vfs_issynchronous)*