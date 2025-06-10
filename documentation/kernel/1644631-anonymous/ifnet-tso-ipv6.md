# IFNET_TSO_IPV6

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
IFNET_TSO_IPV6 = 0x00400000
```

#### Discussion

Hardware supports IPv6 TCP Segment Offloading. If the Interface driver sets this flag, TCP IPv6 will send larger frames (up to 64KB) as one frame to the adapter which will perform the final packetization. The maximum TSO segment supported by the interface can be set with "ifnet_set_tso_mtu". To retreive the real MTU for the TCP IPv6 connection the function "mbuf_get_tso_requested" is used by the driver. Note that if TSO is active, all the packets will be flagged for TSO, not just large packets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1644631-anonymous/ifnet_tso_ipv6)*