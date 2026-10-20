# vfs_setauthopaqueaccess

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Mark a filesystem as having remote VNOP_ACCESS support.

**Availability**:
- macOS 10.4+

## Declaration

```c
void vfs_setauthopaqueaccess(mount_t mp);
```

#### Return Value

void.

## Parameters

- `mp`: Mount to mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523218-vfs_setauthopaqueaccess)*