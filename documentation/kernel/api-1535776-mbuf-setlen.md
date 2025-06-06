# mbuf_setlen

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void mbuf_setlen(mbuf_t mbuf, size_t len);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Sets the length of data in this packet. Be careful to not set the length over the space available in the mbuf.

## Parameters

- `mbuf`: The mbuf.
- `len`: The new length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535776-mbuf_setlen)*