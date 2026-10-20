# operating_modes_t

**Framework**: vmnet  
**Kind**: enum  
**Role**: Enumeration

The operating modes for an interface.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
enum operating_modes_t
```

```c
enum operating_modes_t : uint32_t;
```

## Topics

### Constants
- [operating_modes_t.VMNET_HOST_MODE](./operating_modes_t/vmnet_host_mode.md)
- [operating_modes_t.VMNET_SHARED_MODE](./operating_modes_t/vmnet_shared_mode.md)
### Enumeration cases
- [operating_modes_t.VMNET_BRIDGED_MODE](./operating_modes_t/vmnet_bridged_mode.md)
### Initializers
- [init?(rawValue: UInt32)](./operating_modes_t/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data types
- [enum vmnet_return_t](./vmnet_return_t.md)
  Values returned by functions in the vmnet Framework.
- [struct vmpktdesc](./vmpktdesc.md)
  Describes a packet.
- [typealias interface_ref](./interface_ref.md)
  A virtual network interface.
- [struct interface_event_t](./interface_event_t.md)
  Interface event types.
- [typealias vmnet_mode_t](./vmnet_mode_t.md)
  A type that defines the operating modes of the vmnet interface.
- [typealias vmnet_network_ref](./vmnet_network_ref.md)
  A pointer to a network structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/operating_modes_t)*