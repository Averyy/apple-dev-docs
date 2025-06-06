# mbuf_datastart

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void * mbuf_datastart(mbuf_t mbuf);
```

#### Return_value

A pointer to smallest possible value for data.

#### Discussion

Returns the start of the space set aside for storing data in an mbuf. An mbuf's data may come from a cluster or be embedded in the mbuf structure itself. The data pointer retrieved by mbuf_data may not be at the start of the data (mbuf_leadingspace will be non-zero). This function will return a pointer that matches mbuf_data() - mbuf_leadingspace().

## Parameters

- `mbuf`: The mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535666-mbuf_datastart)*