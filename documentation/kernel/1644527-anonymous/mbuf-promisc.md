# MBUF_PROMISC

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
MBUF_PROMISC = 0x2000
```

#### Discussion

Indicates this packet was only received because the interface is in promiscuous mode. This should be set by the demux function. These packets will be discarded after being passed to any interface filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1644527-anonymous/mbuf_promisc)*