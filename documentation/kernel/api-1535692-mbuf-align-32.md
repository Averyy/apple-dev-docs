# mbuf_align_32

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_align_32(mbuf_t mbuf, size_t len);
```

#### Return_value

0 on success, errno error on failure.

#### Discussion

mbuf_align_32 is a replacement for M_ALIGN and MH_ALIGN. mbuf_align_32 will set the data pointer to a location aligned on a four byte boundry with at least 'len' bytes between the data pointer and the end of the data block.

## Parameters

- `mbuf`: The mbuf.
- `len`: The minimum length of space that should follow the new data location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535692-mbuf_align_32)*