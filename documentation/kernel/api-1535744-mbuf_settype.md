# mbuf_settype

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
errno_t mbuf_settype(mbuf_t mbuf, mbuf_type_t new_type);
```

## Return Value

0 upon success otherwise the errno error.

## Discussion

Sets the type of mbuf.

## Parameters

- `mbuf`: The mbuf.
- `new_type`: The new type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535744-mbuf_settype)*