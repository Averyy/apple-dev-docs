# mbuf_set_csum_performed

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_set_csum_performed(mbuf_t mbuf, mbuf_csum_performed_flags_t flags, u_int32_t value);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

This is used by the driver to indicate to the stack which checksum operations were performed in hardware.

## Parameters

- `mbuf`: The mbuf containing the packet.
- `flags`: Flags indicating which hardware checksum operations were performed.
- `value`: If the MBUF_CSUM_DID_DATA flag is set, value should be set to the value of the TCP or UDP header as calculated by the hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535789-mbuf_set_csum_performed)*