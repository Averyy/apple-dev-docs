# vfs_authopaqueaccess

**Framework**: Kernel  
**Kind**: func

Check if a filesystem is marked as having reliable remote VNOP_ACCESS support.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_authopaqueaccess(mount_t mp);
```

#### Return_value

Nonzero if VNOP_ACCESS is supported remotely, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523247-vfs_authopaqueaccess)*