# mbuf_get_vlan_tag

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_get_vlan_tag(mbuf_t mbuf, u_int16_t *vlan);
```

#### Return_value

0 upon success otherwise the errno error. ENXIO indicates that the vlan tag is not set.

#### Discussion

This function is used by drivers that support hardware vlan tagging to determine which vlan this packet belongs to. To differentiate between the case where the vlan tag is zero and the case where there is no vlan tag, this function will return ENXIO when there is no vlan.

## Parameters

- `mbuf`: The mbuf containing the packet.
- `vlan`: The protocol family of the aux data to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535803-mbuf_get_vlan_tag)*