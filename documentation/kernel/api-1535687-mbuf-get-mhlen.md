# mbuf_get_mhlen

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
u_int32_t mbuf_get_mhlen(void);
```

#### Return_value

The number of bytes of available data.

#### Discussion

This routine returns the number of data bytes in a packet header mbuf. This is equivalent to the legacy MHLEN macro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535687-mbuf_get_mhlen)*