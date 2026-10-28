# mbuf_setlen

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
void mbuf_setlen(mbuf_t mbuf, size_t len);
```

## Return Value

0 upon success otherwise the errno error.

## Discussion

Sets the length of data in this packet. Be careful to not set the length over the space available in the mbuf.

## Parameters

- `mbuf`: The mbuf.
- `len`: The new length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535776-mbuf_setlen)*