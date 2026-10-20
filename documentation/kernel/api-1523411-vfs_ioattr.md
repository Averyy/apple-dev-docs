# vfs_ioattr

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Get I/O attributes associated with a mounpoint.

**Availability**:
- macOS 10.4+

## Declaration

```c
void vfs_ioattr(mount_t mp, struct vfsioattr *ioattrp);
```

#### Return Value

void.

## Parameters

- `mp`: Mount for which to get attributes. If NULL, system defaults are filled into ioattrp.
- `ioattrp`: Destination for results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523411-vfs_ioattr)*