# mbuf_free

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
mbuf_t mbuf_free(mbuf_t mbuf);
```

## Return Value

The next mbuf in the chain.

## Discussion

Frees a single mbuf. Not commonly used because it doesn't touch the rest of the mbufs on the chain.

## Parameters

- `mbuf`: The mbuf to free.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535684-mbuf_free)*