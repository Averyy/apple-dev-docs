# mbuf_copyback

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_copyback(mbuf_t mbuf, size_t offset, size_t length, const void *data, mbuf_how_t how);
```

#### Return_value

0 upon success, EINVAL or ENOBUFS upon failure.

#### Discussion

Copies data from a buffer to an mbuf chain. mbuf_copyback will grow the chain to fit the specified buffer.

If mbuf_copydata is unable to allocate enough mbufs to grow the chain, ENOBUFS will be returned. The mbuf chain will be shorter than expected but all of the data up to the end of the mbuf chain will be valid.

If an offset is specified, mbuf_copyback will skip that many bytes in the mbuf chain before starting to write the buffer in to the chain. If the mbuf chain does not contain this many bytes, mbufs will be allocated to create the space.

## Parameters

- `mbuf`: The first mbuf in the chain to copy the data in to.
- `offset`: Offset in bytes to skip before copying data.
- `length`: The length, in bytes, of the data to copy in to the mbuf chain.
- `data`: A pointer to data in the kernel's address space.
- `how`: Blocking or non-blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535623-mbuf_copyback)*