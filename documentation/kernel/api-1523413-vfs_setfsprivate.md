# vfs_setfsprivate

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Set filesystem-private mount data.

**Availability**:
- macOS 10.4+

## Declaration

```c
void vfs_setfsprivate(mount_t mp, void *mntdata);
```

## Return Value

Void.

## Discussion

A filesystem generally has an internal mount structure which it attaches to the VFS-level mount structure as part of the mounting process.

## Parameters

- `mp`: Mount for which to set private data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523413-vfs_setfsprivate)*