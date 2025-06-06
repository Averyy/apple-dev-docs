# mbuf_clear_csum_requested

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_clear_csum_requested(mbuf_t mbuf);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

This function clears the checksum request flags.

## Parameters

- `mbuf`: The mbuf containing the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535735-mbuf_clear_csum_requested)*