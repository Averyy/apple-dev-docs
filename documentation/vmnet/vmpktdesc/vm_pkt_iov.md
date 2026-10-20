# vm_pkt_iov

**Framework**: vmnet  
**Kind**: property  
**Role**: Instance Property

An array of packet buffers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
var vm_pkt_iov: UnsafeMutablePointer<iovec>
```

```c
struct iovec * vm_pkt_iov;
```

## See Also

### Fields
- [var vm_flags: UInt32](./vm_flags.md)
  Option flags associated with the packet.
- [var vm_pkt_iovcnt: UInt32](./vm_pkt_iovcnt.md)
  The number of packet buffers in `vm_pkt_iov`.
- [var vm_pkt_size: Int](./vm_pkt_size.md)
  The size of the packet, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmpktdesc/vm_pkt_iov)*