# proto_media_input_v2

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.5+

## Declaration

```swift
typedef errno_t (*proto_media_input_v2)(ifnet_t ifp, protocol_family_t protocol, mbuf_t packet);
```

#### Return_value

If the result is zero, the caller will assume the packets were passed to the protocol. If the result is non-zero and not EJUSTRETURN, the caller will free the packets.

#### Discussion

proto_media_input_v2 is called for all inbound packets for a specific protocol on a specific interface. This function is registered on an interface using ifnet_attach_protocolv2. proto_media_input_v2 differs from proto_media_input in that it will be called for a list of packets instead of once for each individual packet. The frame header can be retrieved using mbuf_pkthdr_header.

## Parameters

- `ifp`: The interface the packet was received on.
- `protocol_family`: The protocol of the packet received.
- `packet`: The packet being input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_media_input_v2)*