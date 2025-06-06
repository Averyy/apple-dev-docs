# vfs_fsprivate

**Framework**: Kernel  
**Kind**: func

Get filesystem-private mount data.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void * vfs_fsprivate(mount_t mp);
```

#### Return_value

Private data.

#### Discussion

A filesystem generally has an internal mount structure which it attaches to the VFS-level mount structure as part of the mounting process.

## Parameters

- `mp`: Mount for which to get private data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523301-vfs_fsprivate)*