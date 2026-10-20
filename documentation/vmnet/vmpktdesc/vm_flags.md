# vm_flags

**Framework**: vmnet  
**Kind**: property  
**Role**: Instance Property

Option flags associated with the packet.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
var vm_flags: UInt32
```

```c
uint32_t vm_flags;
```

#### Discussion

Should be set to `0` on read.

## See Also

### Fields
- [var vm_pkt_iov: UnsafeMutablePointer<iovec>](./vm_pkt_iov.md)
  An array of packet buffers.
- [var vm_pkt_iovcnt: UInt32](./vm_pkt_iovcnt.md)
  The number of packet buffers in `vm_pkt_iov`.
- [var vm_pkt_size: Int](./vm_pkt_size.md)
  The size of the packet, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmpktdesc/vm_flags)*