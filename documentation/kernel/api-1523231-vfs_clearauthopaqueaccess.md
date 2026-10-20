# vfs_clearauthopaqueaccess

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Mark a filesystem as not having remote VNOP_ACCESS support.

**Availability**:
- macOS 10.4+

## Declaration

```c
void vfs_clearauthopaqueaccess(mount_t mp);
```

#### Return Value

void.

## Parameters

- `mp`: Mount to mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523231-vfs_clearauthopaqueaccess)*