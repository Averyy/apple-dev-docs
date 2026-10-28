# mbuf_get_minclsize

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
u_int32_t mbuf_get_minclsize(void);
```

## Return Value

The minimum number of bytes before a cluster will be used.

## Discussion

This routine returns the minimum number of data bytes before an external cluster is used. This is equivalent to the legacy MINCLSIZE macro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535737-mbuf_get_minclsize)*