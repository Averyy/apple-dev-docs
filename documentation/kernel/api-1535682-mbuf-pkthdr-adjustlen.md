# mbuf_pkthdr_adjustlen

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void mbuf_pkthdr_adjustlen(mbuf_t mbuf, int amount);
```

#### Discussion

Adjusts the length of the packet in the packet header.

## Parameters

- `mbuf`: The mbuf containing the packet header.
- `amount`: The number of bytes to adjust the packet header length field by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535682-mbuf_pkthdr_adjustlen)*