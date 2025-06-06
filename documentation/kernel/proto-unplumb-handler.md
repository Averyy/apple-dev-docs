# proto_unplumb_handler

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef void (*proto_unplumb_handler)(ifnet_t ifp, protocol_family_t protocol);
```

#### Discussion

proto_unplumb_handler is called to detach a protocol from an interface. A typical unplumb function would call ifnet_detach_protocol and perform any necessary cleanup.

## Parameters

- `ifp`: The interface the protocol should be detached from.
- `protocol_family`: The protocol that should be detached from the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_unplumb_handler)*