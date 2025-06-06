# mbuf_pullup

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_pullup(mbuf_t *mbuf, size_t len);
```

#### Return_value

0 upon success otherwise the errno error. In the case of an error, the mbuf chain has been freed.

#### Discussion

Move the next len bytes in to mbuf from other mbufs in the chain. This is commonly used to get the IP and TCP or UDP header contiguous in the first mbuf. If mbuf_pullup fails, the entire mbuf chain will be freed.

## Parameters

- `mbuf`: The mbuf in the chain the data should be contiguous in.
- `len`: The number of bytes to pull from the next mbuf(s).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535805-mbuf_pullup)*