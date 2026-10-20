# vm_pkt_size

**Framework**: vmnet  
**Kind**: property  
**Role**: Instance Property

The size of the packet, in bytes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
var vm_pkt_size: Int
```

```c
size_t vm_pkt_size;
```

## See Also

### Fields
- [var vm_flags: UInt32](./vm_flags.md)
  Option flags associated with the packet.
- [var vm_pkt_iov: UnsafeMutablePointer<iovec>](./vm_pkt_iov.md)
  An array of packet buffers.
- [var vm_pkt_iovcnt: UInt32](./vm_pkt_iovcnt.md)
  The number of packet buffers in `vm_pkt_iov`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmpktdesc/vm_pkt_size)*