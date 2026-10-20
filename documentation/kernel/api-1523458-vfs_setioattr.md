# vfs_setioattr

**Framework**: Kernel  
**Kind**: func

Set I/O attributes associated with a mounpoint.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_setioattr(mount_t mp, struct vfsioattr *ioattrp);
```

#### Return_value

void.

## Parameters

- `mp`: Mount for which to set attributes.
- `ioattrp`: Structure containing I/O parameters; all fields must be filled in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523458-vfs_setioattr)*