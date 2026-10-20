# vfs_fsprivate

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Get filesystem-private mount data.

**Availability**:
- macOS 10.4+

## Declaration

```c
void * vfs_fsprivate(mount_t mp);
```

#### Return Value

Private data.

#### Discussion

A filesystem generally has an internal mount structure which it attaches to the VFS-level mount structure as part of the mounting process.

## Parameters

- `mp`: Mount for which to get private data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523301-vfs_fsprivate)*