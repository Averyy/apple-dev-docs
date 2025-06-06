# mbuf_prepend

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_prepend(mbuf_t *mbuf, size_t len, mbuf_how_t how);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Prepend len bytes to an mbuf. If there is space (mbuf_leadingspace >= len), the mbuf's data ptr is changed and the same mbuf is returned. If there is no space, a new mbuf may be allocated and prepended to the mbuf chain. If the operation fails, the mbuf may be freed (*mbuf will be NULL).

## Parameters

- `mbuf`: The mbuf to prepend data to. This may change if a new mbuf must be allocated or may be NULL if the operation fails.
- `len`: The length, in bytes, to be prepended to the mbuf.
- `how`: Blocking or non-blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535660-mbuf_prepend)*