# mbuf_maxlen

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
size_t mbuf_maxlen(const mbuf_t mbuf);
```

#### Return_value

The maximum lenght of data for this mbuf.

#### Discussion

Retrieves the maximum length of data that may be stored in this mbuf. This value assumes that the data pointer was set to the start of the possible range for that pointer (mbuf_data_start).

## Parameters

- `mbuf`: The mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535774-mbuf_maxlen)*