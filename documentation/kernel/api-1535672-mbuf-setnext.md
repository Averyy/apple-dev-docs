# mbuf_setnext

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_setnext(mbuf_t mbuf, mbuf_t next);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Sets the next mbuf in the chain.

## Parameters

- `mbuf`: The mbuf.
- `next`: The new next mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535672-mbuf_setnext)*