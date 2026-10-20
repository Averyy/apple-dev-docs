# vm_pkt_iovcnt

**Framework**: vmnet  
**Kind**: property  
**Role**: Instance Property

The number of packet buffers in `vm_pkt_iov`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
var vm_pkt_iovcnt: UInt32
```

```c
uint32_t vm_pkt_iovcnt;
```

## See Also

### Fields
- [var vm_flags: UInt32](./vm_flags.md)
  Option flags associated with the packet.
- [var vm_pkt_iov: UnsafeMutablePointer<iovec>](./vm_pkt_iov.md)
  An array of packet buffers.
- [var vm_pkt_size: Int](./vm_pkt_size.md)
  The size of the packet, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmpktdesc/vm_pkt_iovcnt)*