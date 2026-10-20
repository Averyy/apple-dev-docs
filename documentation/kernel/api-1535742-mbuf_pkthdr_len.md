# mbuf_pkthdr_len

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
size_t mbuf_pkthdr_len(const mbuf_t mbuf);
```

#### Return Value

The length, in bytes, of the packet.

#### Discussion

Returns the length as reported by the packet header.

## Parameters

- `mbuf`: The mbuf containing the packet header with the length to be changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535742-mbuf_pkthdr_len)*