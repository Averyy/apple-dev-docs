# vm_pkt_size

**Framework**: Vmnet  
**Kind**: property

The size of the packet, in bytes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
var vm_pkt_size: Int
```

## See Also

- [var vm_flags: UInt32](vmpktdesc/vm_flags.md)
  Option flags. Should be set to `0` on read.
- [var vm_pkt_iov: UnsafeMutablePointer<iovec>](vmpktdesc/vm_pkt_iov.md)
  An array of packet buffers.
- [var vm_pkt_iovcnt: UInt32](vmpktdesc/vm_pkt_iovcnt.md)
  The number of packet buffers in `vm_pkt_iov`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmpktdesc/vm_pkt_size)*