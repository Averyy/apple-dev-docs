# mbuf_get_csum_requested

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_get_csum_requested(mbuf_t mbuf, mbuf_csum_request_flags_t *request, u_int32_t *value);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

This function is used by the driver to determine which checksum operations should be performed in hardware.

## Parameters

- `mbuf`: The mbuf containing the packet.
- `request`: Flags indicating which checksums are being requested for this packet.
- `value`: This parameter is currently unsupported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535698-mbuf_get_csum_requested)*