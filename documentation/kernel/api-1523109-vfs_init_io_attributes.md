# vfs_init_io_attributes

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Set I/O attributes on a mountpoint based on device properties.

**Availability**:
- macOS 10.6+

## Declaration

```c
int vfs_init_io_attributes(vnode_t devvp, mount_t mp);
```

#### Return Value

0 for success, else an error code.

## Parameters

- `devvp`: Block device vnode from which a filesystem is being mounted.
- `mp`: Mountpoint whose I/O parameters to initialize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523109-vfs_init_io_attributes)*