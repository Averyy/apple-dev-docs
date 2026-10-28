# vfs_isreload

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Determine if a reload of filesystem data is in progress. This can only be the case for a read-only filesystem; all data is brought in from secondary storage.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_isreload(mount_t mp);
```

## Return Value

Nonzero if a request has been made to reload data, else 0.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523537-vfs_isreload)*