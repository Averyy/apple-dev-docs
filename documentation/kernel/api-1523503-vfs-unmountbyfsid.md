# vfs_unmountbyfsid

**Framework**: Kernel  
**Kind**: func

Find a filesystem by ID and unmount it.

**Availability**:
- macOS 10.5+

## Declaration

```swift
int vfs_unmountbyfsid(fsid_t *fsid, int flags, vfs_context_t ctx);
```

#### Return_value

0 for succcess, nonero for failure.

## Parameters

- `fsid`: ID of filesystem to unmount, as found through (for example) statfs.
- `flags`: MNT_FORCE: forcibly invalidate files open on the mount (though in-flight I/O operations will be allowed to complete).
- `ctx`: Context against which to authenticate unmount operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523503-vfs_unmountbyfsid)*