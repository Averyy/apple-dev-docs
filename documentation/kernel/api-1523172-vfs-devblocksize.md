# vfs_devblocksize

**Framework**: Kernel  
**Kind**: func

Get the block size of the device underlying a mount.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_devblocksize(mount_t mp);
```

#### Return_value

Block size.

## Parameters

- `mp`: Mount for which to get block size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523172-vfs_devblocksize)*