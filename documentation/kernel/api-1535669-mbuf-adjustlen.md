# mbuf_adjustlen

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_adjustlen(mbuf_t mbuf, int amount);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Adds amount to the mbuf len. Verifies that the new length is valid (greater than or equal to zero and less than maximum amount of data that may be stored in the mbuf). This function will not adjust the packet header length field or affect any other mbufs in a chain.

## Parameters

- `mbuf`: The mbuf to adjust.
- `amount`: The number of bytes increment the length by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535669-mbuf_adjustlen)*