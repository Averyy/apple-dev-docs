# mbuf_gethdr

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_gethdr(mbuf_how_t how, mbuf_type_t type, mbuf_t *mbuf);
```

#### Return_value

0 on success, errno error on failure.

#### Discussion

Allocates an mbuf without a cluster for external data. Sets a flag to indicate there is a packet header and initializes the packet header.

## Parameters

- `how`: Blocking or non-blocking.
- `type`: The type of the mbuf.
- `mbuf`: The mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535722-mbuf_gethdr)*