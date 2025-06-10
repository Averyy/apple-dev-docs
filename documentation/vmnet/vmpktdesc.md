# vmpktdesc

**Framework**: vmnet  
**Kind**: struct

Describes a packet.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
struct vmpktdesc
```

## Topics

### Fields
- [var vm_flags: UInt32](vmpktdesc/vm_flags.md)
  Option flags. Should be set to `0` on read.
- [var vm_pkt_iov: UnsafeMutablePointer<iovec>](vmpktdesc/vm_pkt_iov.md)
  An array of packet buffers.
- [var vm_pkt_iovcnt: UInt32](vmpktdesc/vm_pkt_iovcnt.md)
  The number of packet buffers in `vm_pkt_iov`.
- [var vm_pkt_size: Int](vmpktdesc/vm_pkt_size.md)
  The size of the packet, in bytes.
### Initializers
- [init(vm_pkt_size: Int, vm_pkt_iov: UnsafeMutablePointer<iovec>, vm_pkt_iovcnt: UInt32, vm_flags: UInt32)](vmpktdesc/init(vm_pkt_size:vm_pkt_iov:vm_pkt_iovcnt:vm_flags:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [enum vmnet_return_t](vmnet_return_t.md)
  Values returned by functions in the vmnet Framework.
- [typealias interface_ref](interface_ref.md)
  A virtual network interface.
- [struct interface_event_t](interface_event_t.md)
  Interface event types.
- [enum operating_modes_t](operating_modes_t.md)
  The operating modes for an interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmpktdesc)*