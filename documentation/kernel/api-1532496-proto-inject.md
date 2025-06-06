# proto_inject

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t proto_inject(protocol_family_t protocol, mbuf_t packet);
```

#### Return_value

A errno error on failure. Unless proto_inject returns zero, the caller is responsible for freeing the mbuf.

#### Discussion

Injects a packet on the specified protocol from anywhere. To avoid recursion, the protocol may need to queue the packet to be handled later.

## Parameters

- `protocol`: The protocol of the packet.
- `packet`: The first packet in a chain of packets to be injected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532496-proto_inject)*