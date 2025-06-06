# physio

**Framework**: Kernel  
**Kind**: func

Perform I/O on a device to/from target memory described by a uio.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int physio(void (*f_strategy)(buf_t), buf_t bp, dev_t dev, int flags, u_int (*f_minphys)(buf_t), struct uio *uio, int blocksize);
```

#### Return_value

0 for success; EFAULT for an invalid uio; errors from buf_biowait().

#### Discussion

physio() allows I/O directly from a device to user-space memory. It waits for all I/O to complete before returning.

## Parameters

- `f_strategy`: Strategy routine to call to initiate I/O.
- `bp`: Buffer to configure and pass to strategy routine; can be NULL.
- `dev`: Device on which to perform I/O.
- `flags`: B_READ or B_WRITE.
- `f_minphys`: Function which calls buf_setcount() to set a byte count which is suitably small for the device in question. Returns byte count that has been set (or unchanged) on the buffer.
- `uio`: UIO describing the I/O operation.
- `blocksize`: Logical block size for this vnode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1561895-physio)*