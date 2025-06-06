# proto_media_event

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef void (*proto_media_event)(ifnet_t ifp, protocol_family_t protocol, const struct kev_msg *event);
```

#### Discussion

proto_media_event is called to notify this layer of interface specific events.

## Parameters

- `ifp`: The interface.
- `protocol_family`: The protocol family.
- `kev_msg`: The event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_media_event)*