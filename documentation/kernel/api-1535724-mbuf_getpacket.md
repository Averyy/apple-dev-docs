# mbuf_getpacket

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
errno_t mbuf_getpacket(mbuf_how_t how, mbuf_t *mbuf);
```

#### Return Value

0 on success, errno error on failure.

#### Discussion

Allocate an mbuf, allocate and attach a cluster, and set the packet header flag.

## Parameters

- `how`: Blocking or non-blocking.
- `mbuf`: Upon success, *mbuf will be a reference to the new mbuf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535724-mbuf_getpacket)*