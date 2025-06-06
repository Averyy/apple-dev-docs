# mbuf_copy_pkthdr

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_copy_pkthdr(mbuf_t dest, const mbuf_t src);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Copies the packet header from src to dest.

## Parameters

- `src`: The mbuf from which the packet header will be copied.
- `mbuf`: The mbuf to which the packet header will be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535645-mbuf_copy_pkthdr)*