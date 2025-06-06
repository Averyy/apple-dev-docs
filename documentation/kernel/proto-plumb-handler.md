# proto_plumb_handler

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*proto_plumb_handler)(ifnet_t ifp, protocol_family_t protocol);
```

#### Return_value

A non-zero value of the attach failed.

#### Discussion

proto_plumb_handler is called to attach a protocol to an interface. A typical protocol plumb function would fill out an ifnet_attach_proto_param and call ifnet_attach_protocol.

## Parameters

- `ifp`: The interface the protocol should be attached to.
- `protocol_family`: The protocol that should be attached to the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_plumb_handler)*