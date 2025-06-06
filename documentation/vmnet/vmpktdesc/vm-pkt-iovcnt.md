# vm_pkt_iovcnt

**Framework**: Vmnet  
**Kind**: property

The number of packet buffers in `vm_pkt_iov`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
var vm_pkt_iovcnt: UInt32
```

## See Also

- [var vm_flags: UInt32](vmpktdesc/vm_flags.md)
  Option flags. Should be set to `0` on read.
- [var vm_pkt_iov: UnsafeMutablePointer<iovec>](vmpktdesc/vm_pkt_iov.md)
  An array of packet buffers.
- [var vm_pkt_size: Int](vmpktdesc/vm_pkt_size.md)
  The size of the packet, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmpktdesc/vm_pkt_iovcnt)*