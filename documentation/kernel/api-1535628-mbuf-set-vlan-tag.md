# mbuf_set_vlan_tag

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_set_vlan_tag(mbuf_t mbuf, u_int16_t vlan);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

This function is used by interfaces that support vlan tagging in hardware. This function will set properties in the mbuf to indicate which vlan the packet was received for.

## Parameters

- `mbuf`: The mbuf containing the packet.
- `vlan`: The protocol family of the aux data to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535628-mbuf_set_vlan_tag)*