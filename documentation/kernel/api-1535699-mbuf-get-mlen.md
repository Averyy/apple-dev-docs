# mbuf_get_mlen

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
u_int32_t mbuf_get_mlen(void);
```

#### Return_value

The number of bytes of available data.

#### Discussion

This routine returns the number of data bytes in a normal mbuf, i.e. an mbuf that is not a packet header, nor one with an external cluster attached to it. This is equivalent to the legacy MLEN macro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535699-mbuf_get_mlen)*