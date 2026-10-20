# vfs_fsadd

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Register a filesystem with VFS.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_fsadd(struct vfs_fsentry *vfe, vfstable_t *handle);
```

#### Return Value

0 for success, else an error code.

#### Discussion

Typically called by a filesystem Kernel Extension when it is loaded.

## Parameters

- `vfe`: Filesystem information: table of vfs operations, list of vnode operation tables, filesystem type number (can be omitted with VFS_TBLNOTYPENUM flag), name, flags.
- `handle`: Opaque handle which will be passed to vfs_fsremove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523490-vfs_fsadd)*