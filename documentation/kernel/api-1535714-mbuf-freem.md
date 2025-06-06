# mbuf_freem

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void mbuf_freem(mbuf_t mbuf);
```

#### Discussion

Frees a chain of mbufs link through mnext.

## Parameters

- `mbuf`: The first mbuf in the chain to free.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535714-mbuf_freem)*