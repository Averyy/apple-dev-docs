# operating_modes_t

**Framework**: Vmnet  
**Kind**: enum

The operating modes for an interface.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
enum operating_modes_t
```

## Topics

### Constants
- [operating_modes_t.VMNET_HOST_MODE](operating_modes_t/vmnet_host_mode.md)
- [operating_modes_t.VMNET_SHARED_MODE](operating_modes_t/vmnet_shared_mode.md)
### Enumeration cases
- [operating_modes_t.VMNET_BRIDGED_MODE](operating_modes_t/vmnet_bridged_mode.md)
### Initializers
- [init?(rawValue: UInt32)](operating_modes_t/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum vmnet_return_t](vmnet_return_t.md)
  Values returned by functions in the vmnet Framework.
- [struct vmpktdesc](vmpktdesc.md)
  Describes a packet.
- [typealias interface_ref](interface_ref.md)
  A virtual network interface.
- [struct interface_event_t](interface_event_t.md)
  Interface event types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/operating_modes_t)*