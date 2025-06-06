# vfs_setfsprivate

**Framework**: Kernel  
**Kind**: func

Set filesystem-private mount data.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_setfsprivate(mount_t mp, void *mntdata);
```

#### Return_value

Void.

#### Discussion

A filesystem generally has an internal mount structure which it attaches to the VFS-level mount structure as part of the mounting process.

## Parameters

- `mp`: Mount for which to set private data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523413-vfs_setfsprivate)*