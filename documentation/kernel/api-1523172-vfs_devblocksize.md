# vfs_devblocksize

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Get the block size of the device underlying a mount.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_devblocksize(mount_t mp);
```

## Return Value

Block size.

## Parameters

- `mp`: Mount for which to get block size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523172-vfs_devblocksize)*