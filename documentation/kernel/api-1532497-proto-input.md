# proto_input

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t proto_input(protocol_family_t protocol, mbuf_t packet);
```

#### Return_value

A errno error on failure. Unless proto_input returns zero, the caller is responsible for freeing the mbuf.

#### Discussion

Inputs a packet on the specified protocol from the input path.

## Parameters

- `protocol`: The protocol of the packet.
- `packet`: The first packet in a chain of packets to be input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532497-proto_input)*