# vfs_authopaqueaccess

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Check if a filesystem is marked as having reliable remote VNOP_ACCESS support.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_authopaqueaccess(mount_t mp);
```

## Return Value

Nonzero if VNOP_ACCESS is supported remotely, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523247-vfs_authopaqueaccess)*