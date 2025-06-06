# mbuf_leadingspace

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
size_t mbuf_leadingspace(const mbuf_t mbuf);
```

#### Return_value

The number of unused bytes at the start of the mbuf.

#### Discussion

Determines the space available in the mbuf proceeding the current data.

## Parameters

- `mbuf`: The mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535767-mbuf_leadingspace)*