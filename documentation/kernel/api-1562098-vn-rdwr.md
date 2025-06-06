# vn_rdwr

**Framework**: Kernel  
**Kind**: func

Read from or write to a file.

**Availability**:
- macOS 10.6+

## Declaration

```swift
int vn_rdwr(enum uio_rw rw, struct vnode *vp, caddr_t base, int len, off_t offset, enum uio_seg segflg, int ioflg, kauth_cred_t cred, int *aresid, proc_t p);
```

#### Return_value

0 for success; errors from filesystem, and EIO if did not perform all requested I/O and the "aresid" parameter is NULL.

#### Discussion

vn_rdwr() abstracts the details of constructing a uio and picking a vnode operation to allow simple in-kernel file I/O.

## Parameters

- `rw`: UIO_READ for a read, UIO_WRITE for a write.
- `vp`: The vnode on which to perform I/O.
- `base`: Start of buffer into which to read or from which to write data.
- `len`: Length of buffer.
- `offset`: Offset within the file at which to start I/O.
- `segflg`: What kind of address "base" is. See uio_seg definition in sys/uio.h. UIO_SYSSPACE for kernelspace, UIO_USERSPACE for userspace. UIO_USERSPACE32 and UIO_USERSPACE64 are in general preferred, but vn_rdwr will make sure that has the correct address sizes.
- `ioflg`: Defined in vnode.h, e.g. IO_NOAUTH, IO_NOCACHE.
- `cred`: Credential to pass down to filesystem for authentication.
- `aresid`: Destination for amount of requested I/O which was not completed, as with uio_resid().
- `p`: Process requesting I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562098-vn_rdwr)*