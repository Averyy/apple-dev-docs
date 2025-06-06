# mbuf_pkthdr_setlen

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void mbuf_pkthdr_setlen(mbuf_t mbuf, size_t len);
```

#### Discussion

Sets the length of the packet in the packet header.

## Parameters

- `mbuf`: The mbuf containing the packet header.
- `len`: The new length of the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535646-mbuf_pkthdr_setlen)*