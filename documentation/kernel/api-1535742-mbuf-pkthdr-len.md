# mbuf_pkthdr_len

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
size_t mbuf_pkthdr_len(const mbuf_t mbuf);
```

#### Return_value

The length, in bytes, of the packet.

#### Discussion

Returns the length as reported by the packet header.

## Parameters

- `mbuf`: The mbuf containing the packet header with the length to be changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535742-mbuf_pkthdr_len)*