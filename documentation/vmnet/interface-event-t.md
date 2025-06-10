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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [enum vmnet_return_t](vmnet_return_t.md)
  Values returned by functions in the vmnet Framework.
- [struct vmpktdesc](vmpktdesc.md)
  Describes a packet.
- [typealias interface_ref](interface_ref.md)
  A virtual network interface.
- [enum operating_modes_t](operating_modes_t.md)
  The operating modes for an interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/interface_event_t)*