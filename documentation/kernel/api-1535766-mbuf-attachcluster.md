# mbuf_attachcluster

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_attachcluster(mbuf_how_t how, mbuf_type_t type, mbuf_t *mbuf, caddr_t extbuf, void (*extfree)(caddr_t, u_int, caddr_t), size_t extsize, caddr_t extarg);
```

#### Return_value

0 on success EINVAL - Invalid parameter ENOMEM - Not enough memory available

#### Discussion

Attach an external buffer as a cluster for an mbuf. If mbuf points to a NULL mbuf_t, an mbuf will be allocated for you. If mbuf points to a non-NULL mbuf_t, the user-supplied mbuf will be used instead. The caller is responsible for allocating the external buffer by calling mbuf_alloccluster().

## Parameters

- `how`: Blocking or non-blocking.
- `type`: The type of the mbuf if mbuf is non-NULL; otherwise ignored.
- `mbuf`: Pointer to the address of the mbuf; if NULL, an mbuf will be allocated, otherwise, it must point to a valid mbuf address. If the user-supplied mbuf is already attached to a cluster, the current cluster will be freed before the mbuf gets attached to the supplied external buffer. Note that this routine may return a different mbuf_t than the one you passed in.
- `extbuf`: Address of the external buffer.
- `extfree`: Free routine for the external buffer; the caller is required to defined a routine that will be invoked when the mbuf is freed.
- `extsize`: Size of the external buffer.
- `extarg`: Private value that will be passed to the free routine when it is called at the time the mbuf is freed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535766-mbuf_attachcluster)*