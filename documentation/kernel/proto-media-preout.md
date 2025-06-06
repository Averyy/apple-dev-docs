# proto_media_preout

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*proto_media_preout)(ifnet_t ifp, protocol_family_t protocol, mbuf_t *packet, const struct sockaddr *dest, void *route, char *frame_type, char *link_layer_dest);
```

#### Return_value

If the result is zero, processing will continue normally. If the result is non-zero, processing will stop. If the result is non-zero and not EJUSTRETURN, the packet will be freed by the caller.

#### Discussion

proto_media_preout is called just before the packet is transmitted. This gives the proto_media_preout function an opportunity to specify the media specific frame type and destination.

## Parameters

- `ifp`: The interface the packet will be sent on.
- `protocol_family`: The protocol of the packet being sent (PF_INET/etc...).
- `packet`: The packet being sent.
- `dest`: The protocol level destination address.
- `route`: A pointer to the routing structure for the packet.
- `frame_type`: The media specific frame type.
- `link_layer_dest`: The media specific destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_media_preout)*