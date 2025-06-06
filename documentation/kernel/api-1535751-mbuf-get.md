# mbuf_get

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_get(mbuf_how_t how, mbuf_type_t type, mbuf_t *mbuf);
```

#### Return_value

0 on success, errno error on failure.

#### Discussion

Allocates an mbuf without a cluster for external data.

## Parameters

- `how`: Blocking or non-blocking.
- `type`: The type of the mbuf.
- `mbuf`: The mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535751-mbuf_get)*