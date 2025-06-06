# mbuf_mclget

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_mclget(mbuf_how_t how, mbuf_type_t type, mbuf_t *mbuf);
```

#### Return_value

0 on success, errno error on failure. If you specified NULL for the mbuf, any intermediate mbuf that may have been allocated will be freed. If you specify an mbuf value in *mbuf, mbuf_mclget will not free it.

#### Discussion

Allocate a cluster and attach it to an mbuf for use as external data. If mbuf points to a NULL mbuf_t, an mbuf will be allocated for you. If mbuf points to a non-NULL mbuf_t, mbuf_mclget may return a different mbuf_t than the one you passed in.

## Parameters

- `how`: Blocking or non-blocking.
- `type`: The type of the mbuf.
- `mbuf`: The mbuf the cluster will be attached to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535664-mbuf_mclget)*