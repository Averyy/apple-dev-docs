# proto_media_input

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*proto_media_input)(ifnet_t ifp, protocol_family_t protocol, mbuf_t packet, char *header);
```

#### Return_value

If the result is zero, the caller will assume the packet was passed to the protocol. If the result is non-zero and not EJUSTRETURN, the caller will free the packet.

#### Discussion

proto_media_input is called for all inbound packets for a specific protocol on a specific interface. This function is registered on an interface using ifnet_attach_protocol.

## Parameters

- `ifp`: The interface the packet was received on.
- `protocol_family`: The protocol of the packet received.
- `packet`: The packet being input.
- `header`: The frame header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_media_input)*