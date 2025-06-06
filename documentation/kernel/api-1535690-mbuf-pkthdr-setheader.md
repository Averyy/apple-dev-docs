# mbuf_pkthdr_setheader

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void mbuf_pkthdr_setheader(mbuf_t mbuf, void *header);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Sets the pointer to the packet header.

## Parameters

- `mbuf`: The mbuf containing the packet header.
- `ifnet`: A pointer to the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535690-mbuf_pkthdr_setheader)*