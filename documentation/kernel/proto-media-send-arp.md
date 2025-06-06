# proto_media_send_arp

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*proto_media_send_arp)(ifnet_t ifp, u_short arpop, const struct sockaddr_dl *sender_hw, const struct sockaddr *sender_proto, const struct sockaddr_dl *target_hw, const struct sockaddr *target_proto);
```

#### Return_value

Return zero on success or an errno error value on failure.

#### Discussion

proto_media_send_arp is called by the stack to generate an ARP packet. This field is currently only used with IP. This function should inspect the parameters and transmit an arp packet using the information passed in.

## Parameters

- `ifp`: The interface the arp packet should be sent on.
- `protocol_family`: The protocol family of the addresses (PF_INET).
- `arpop`: The arp operation (usually ARPOP_REQUEST or ARPOP_REPLY).
- `sender_hw`: The value to use for the sender hardware address field. If this is NULL, use the hardware address of the interface.
- `sender_proto`: The value to use for the sender protocol address field. This will not be NULL.
- `target_hw`: The value to use for the target hardware address. If this is NULL, the target hardware address in the ARP packet should be NULL and the link-layer destination for the back should be a broadcast. If this is not NULL, this value should be used for both the link-layer destination and the target hardware address.
- `target_proto`: The target protocol address. This will not be NULL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_media_send_arp)*