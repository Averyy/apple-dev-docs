# vfs_setauthopaque

**Framework**: Kernel  
**Kind**: func

Mark a filesystem as having authorization decisions controlled remotely.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_setauthopaque(mount_t mp);
```

#### Return_value

void.

## Parameters

- `mp`: Mount to mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523440-vfs_setauthopaque)*