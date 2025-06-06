# mbuf_setflags

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_setflags(mbuf_t mbuf, mbuf_flags_t flags);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Sets the set of set flags.

## Parameters

- `mbuf`: The mbuf.
- `flags`: The flags that should be set, all other flags will be cleared. Certain flags such as MBUF_EXT cannot be altered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535683-mbuf_setflags)*