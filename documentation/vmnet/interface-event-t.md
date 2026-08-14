# interface_event_t

**Framework**: vmnet  
**Kind**: struct

Interface event types.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
struct interface_event_t
```

## Topics

### Constants
- [static var VMNET_INTERFACE_PACKETS_AVAILABLE: interface_event_t](interface_event_t/vmnet_interface_packets_available.md)
### Initializers
- [init(rawValue: UInt32)](interface_event_t/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [enum vmnet_return_t](vmnet_return_t.md)
  Values returned by functions in the vmnet Framework.
- [struct vmpktdesc](vmpktdesc.md)
  Describes a packet.
- [typealias interface_ref](interface_ref.md)
  A virtual network interface.
- [enum operating_modes_t](operating_modes_t.md)
  The operating modes for an interface.
- [typealias vmnet_mode_t](vmnet_mode_t.md)
  A type that defines the operating modes of the vmnet interface.
- [typealias vmnet_network_ref](vmnet_network_ref.md)
  A pointer to a network structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/interface_event_t)*