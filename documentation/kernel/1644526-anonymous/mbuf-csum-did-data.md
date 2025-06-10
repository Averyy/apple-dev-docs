# MBUF_CSUM_DID_DATA

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
MBUF_CSUM_DID_DATA = 0x0400
```

#### Discussion

Indicates that the TCP or UDP checksum was calculated. The value for the checksum calculated in hardware should be passed as the second parameter of mbuf_set_csum_performed. The hardware calculated checksum value can be retrieved using the second parameter passed to mbuf_get_csum_performed. This should be done for IPv4 or IPv6.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1644526-anonymous/mbuf_csum_did_data)*