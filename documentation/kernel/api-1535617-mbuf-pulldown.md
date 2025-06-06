# mbuf_pulldown

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_pulldown(mbuf_t src, size_t *offset, size_t length, mbuf_t *location);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Make length bytes at offset in the mbuf chain contiguous. Nothing before offset bytes in the chain will be modified. Upon return, location will be the mbuf the data is contiguous in and offset will be the offset in that mbuf at which the data is located. In the case of a failure, the mbuf chain will be freed.

## Parameters

- `src`: The start of the mbuf chain.
- `offset`: Pass in a pointer to a value with the offset of the data you're interested in making contiguous. Upon success, this will be overwritten with the offset from the mbuf returned in location.
- `length`: The length of data that should be made contiguous.
- `location`: Upon success, *location will be the mbuf the data is in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535617-mbuf_pulldown)*