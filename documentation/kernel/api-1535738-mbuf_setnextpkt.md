# mbuf_setnextpkt

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
void mbuf_setnextpkt(mbuf_t mbuf, mbuf_t nextpkt);
```

#### Discussion

Sets the next packet attached to this mbuf.

## Parameters

- `mbuf`: The mbuf.
- `nextpkt`: The new next packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535738-mbuf_setnextpkt)*