# MBUF_DONTWAIT

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.12+

## Declaration

```c
MBUF_DONTWAIT = 1
```

## Discussion

Don't allow the mbuf allocation call to block, if blocking is necessary fail and return immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1644523-anonymous/mbuf_dontwait)*