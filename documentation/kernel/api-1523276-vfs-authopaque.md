# vfs_authopaque

**Framework**: Kernel  
**Kind**: func

Determine if a filesystem's authorization decisions occur remotely.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_authopaque(mount_t mp);
```

#### Return_value

Nonzero if filesystem authorization is controlled remotely, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523276-vfs_authopaque)*