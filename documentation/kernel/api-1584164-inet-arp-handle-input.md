# inet_arp_handle_input

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
errno_t inet_arp_handle_input(ifnet_t ifp, u_int16_t arpop, const struct sockaddr_dl *sender_hw, const struct sockaddr_in *sender_ip, const struct sockaddr_in *target_ip);
```

#### Return_value

0 on success or an errno error value on failure.

#### Discussion

This function should be called by code that handles inbound arp packets. The caller should parse the ARP packet to pull out the operation and the relevant addresses. If a response is required, the proto_media_send_arp function will be called.

This function will lookup the sender in the routing table and add an arp entry if necessary. Any queued packets waiting for the arp resolution will also be transmitted.

## Parameters

- `interface`: The interface the packet was received on.
- `arp_op`: The arp operation, ARPOP_REQUEST or ARPOP_REPLY
- `sender_hw`: The sender hardware address from the arp payload.
- `sender_ip`: The sender IP address from the arp payload.
- `target_ip`: The target IP address from the arp payload.

## See Also

- [inet_arp_init_ifaddr](1584163-inet_arp_init_ifaddr.md)
- [inet_arp_lookup](1584165-inet_arp_lookup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1584164-inet_arp_handle_input)*