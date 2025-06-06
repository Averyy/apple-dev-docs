# vmnet_read(_:_:_:)

**Framework**: Vmnet  
**Kind**: func

Attempts to read a specified number of packets from an interface.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
func vmnet_read(_ interface: interface_ref, _ packets: UnsafeMutablePointer<vmpktdesc>, _ pktcnt: UnsafeMutablePointer<Int32>) -> vmnet_return_t
```

#### Return Value

Returns `vmnet` on success, or an error code on failure. See `vmnet` for possible values.

#### Discussion

Each packet buffer passed should be at least as large as the value of [`vmnet_max_packet_size_key`](vmnet_max_packet_size_key.md) for the interface.

## Parameters

- `interface`: The interface reference.
- `packets`: On return, this parameter is populated with an array of packets read.
- `pktcnt`: The number of packets to read.   On return, this parameter is populated with the number of packets read, or   no packets are available to be read.

## See Also

- [func vmnet_write(interface_ref, UnsafeMutablePointer<vmpktdesc>, UnsafeMutablePointer<Int32>) -> vmnet_return_t](vmnet_write(_:_:_:).md)
  Attempts to write specified packets to an interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_read(_:_:_:))*