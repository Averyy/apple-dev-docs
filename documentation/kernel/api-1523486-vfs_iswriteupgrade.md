# vfs_iswriteupgrade

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Determine if a filesystem is mounted read-only but a request has been made to upgrade to read-write.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_iswriteupgrade(mount_t mp);
```

## Return Value

Nonzero if a request has been made to update from read-only to read-write, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523486-vfs_iswriteupgrade)*