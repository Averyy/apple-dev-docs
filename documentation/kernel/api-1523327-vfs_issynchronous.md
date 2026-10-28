# vfs_issynchronous

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Determine if writes to a filesystem occur synchronously.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_issynchronous(mount_t mp);
```

## Return Value

Nonzero if writes occur synchronously, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523327-vfs_issynchronous)*