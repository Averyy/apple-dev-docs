# mbuf_clear_vlan_tag

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
errno_t mbuf_clear_vlan_tag(mbuf_t mbuf);
```

## Return Value

0 upon success otherwise the errno error.

## Discussion

This function will clear any vlan tag associated with the mbuf.

## Parameters

- `mbuf`: The mbuf containing the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535696-mbuf_clear_vlan_tag)*