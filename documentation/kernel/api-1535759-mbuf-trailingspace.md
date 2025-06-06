# mbuf_trailingspace

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
size_t mbuf_trailingspace(const mbuf_t mbuf);
```

#### Return_value

The number of unused bytes following the current data.

#### Discussion

Determines the space available in the mbuf following the current data.

## Parameters

- `mbuf`: The mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535759-mbuf_trailingspace)*