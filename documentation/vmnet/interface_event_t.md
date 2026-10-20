# interface_event_t

**Framework**: vmnet  
**Kind**: struct  
**Role**: Structure

Interface event types.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
struct interface_event_t
```

```c
enum interface_event_t : uint32_t;
```

## Topics

### Constants
- [static var VMNET_INTERFACE_PACKETS_AVAILABLE: interface_event_t](./interface_event_t/vmnet_interface_packets_available.md)
### Initializers
- [init(rawValue: UInt32)](./interface_event_t/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Data types
- [enum vmnet_return_t](./vmnet_return_t.md)
  Values returned by functions in the vmnet Framework.
- [struct vmpktdesc](./vmpktdesc.md)
  Describes a packet.
- [typealias interface_ref](./interface_ref.md)
  A virtual network interface.
- [enum operating_modes_t](./operating_modes_t.md)
  The operating modes for an interface.
- [typealias vmnet_mode_t](./vmnet_mode_t.md)
  A type that defines the operating modes of the vmnet interface.
- [typealias vmnet_network_ref](./vmnet_network_ref.md)
  A pointer to a network structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/interface_event_t)*