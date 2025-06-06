# mbuf_pkthdr_setrcvif

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_pkthdr_setrcvif(mbuf_t mbuf, ifnet_t ifp);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Sets the interface the packet was received on.

## Parameters

- `mbuf`: The mbuf containing the packet header.
- `ifnet`: A reference to an interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535657-mbuf_pkthdr_setrcvif)*