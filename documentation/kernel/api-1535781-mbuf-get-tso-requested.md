# mbuf_get_tso_requested

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_get_tso_requested(mbuf_t mbuf, mbuf_tso_request_flags_t *request, u_int32_t *mss);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

This function is used by the driver to determine which checksum operations should be performed in hardware.

## Parameters

- `mbuf`: The mbuf containing the packet.
- `request`: Flags indicating which values are being requested for this packet.
- `value`: The requested value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535781-mbuf_get_tso_requested)*