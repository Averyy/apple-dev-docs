# vfs_isforce

**Framework**: Kernel  
**Kind**: func

Determine if a forced unmount is in progress.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_isforce(mount_t mp);
```

#### Return_value

Nonzero if a request has been made to forcibly unmount, else 0.

#### Discussion

A forced unmount invalidates open files.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523525-vfs_isforce)*