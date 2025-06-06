# mbuf_pkthdr_header

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void * mbuf_pkthdr_header(const mbuf_t mbuf);
```

#### Return_value

A pointer to the packet header.

#### Discussion

Returns a pointer to the packet header.

## Parameters

- `mbuf`: The mbuf containing the packet header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535662-mbuf_pkthdr_header)*