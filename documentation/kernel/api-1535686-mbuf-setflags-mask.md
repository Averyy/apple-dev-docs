# mbuf_setflags_mask

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_setflags_mask(mbuf_t mbuf, mbuf_flags_t flags, mbuf_flags_t mask);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Useful for setting or clearing individual flags. Easier than calling mbuf_setflags(m, mbuf_flags(m) | M_FLAG).

## Parameters

- `mbuf`: The mbuf.
- `flags`: The flags that should be set or cleared. Certain flags such as MBUF_EXT cannot be altered.
- `mask`: The mask controlling which flags will be modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535686-mbuf_setflags_mask)*