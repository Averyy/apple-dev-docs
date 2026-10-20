# mbuf_clear_csum_performed

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
errno_t mbuf_clear_csum_performed(mbuf_t mbuf);
```

#### Return Value

0 upon success otherwise the errno error.

#### Discussion

Clears the hardware checksum flags and values.

## Parameters

- `mbuf`: The mbuf containing the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535748-mbuf_clear_csum_performed)*