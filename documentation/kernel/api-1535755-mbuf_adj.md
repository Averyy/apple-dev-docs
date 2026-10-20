# mbuf_adj

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void mbuf_adj(mbuf_t mbuf, int len);
```

#### Discussion

Trims len bytes from the mbuf. If the length is greater than zero, the bytes are trimmed from the front of the mbuf. If the length is less than zero, the bytes are trimmed from the end of the mbuf chain.

## Parameters

- `mbuf`: The mbuf chain to trim.
- `len`: The number of bytes to trim from the mbuf chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535755-mbuf_adj)*