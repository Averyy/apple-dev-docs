# mbuf_inet6_cksum

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_inet6_cksum(mbuf_t mbuf, int protocol, u_int32_t offset, u_int32_t length, u_int16_t *csum);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

@discussions Calculates 16-bit 1's complement Internet checksum of the transport segment with or without the pseudo header checksum of a given IPv6 packet. If the caller specifies a non-zero transport protocol, the checksum returned will also include the pseudo header checksum for the corresponding transport header. Otherwise, no header parsing will be done and the caller may use this to calculate the Internet checksum of an arbitrary span of data.

This routine does not modify the contents of the packet. If the caller specifies a non-zero protocol and/or offset, the routine expects the complete protocol header(s) to be present at the beginning of the first mbuf.

## Parameters

- `mbuf`: The mbuf (or chain of mbufs) containing the packet.
- `protocol`: A zero or non-zero value. A non-zero value specifies the transport protocol used for pseudo header checksum.
- `offset`: A zero or non-zero value; if the latter, it specifies the offset of the transport header from the beginning of mbuf.
- `length`: The total (non-zero) length of the transport segment.
- `csum`: Pointer to the checksum variable; upon success, this routine will return the calculated Internet checksum through this variable. The caller must set it to a non-NULL value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535764-mbuf_inet6_cksum)*