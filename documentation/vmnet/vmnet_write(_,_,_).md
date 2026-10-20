# vmnet_write(_:_:_:)

**Framework**: vmnet  
**Kind**: func  
**Role**: Function

Attempts to write specified packets to an interface.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
func vmnet_write(_ interface: interface_ref, _ packets: UnsafeMutablePointer<vmpktdesc>, _ pktcnt: UnsafeMutablePointer<Int32>) -> vmnet_return_t
```

```c
vmnet_return_t vmnet_write(interface_ref interface, struct vmpktdesc *packets, int *pktcnt);
```

#### Return Value

`vmnet` on success, or an error code on failure. See `vmnet` for possible values.

#### Discussion

None of the packet to be written should exceed the size of the value of [`vmnet_max_packet_size_key`](./vmnet_max_packet_size_key.md) for the interface.

## Parameters

- `interface`: The interface reference.
- `packets`: An array of packets to be written.
- `pktcnt`: The number of packets to write. On return, this parameter is populated with the number of packets the framework wrote.

## See Also

### Reading and Writing Packets
- [func vmnet_read(interface_ref, UnsafeMutablePointer<vmpktdesc>, UnsafeMutablePointer<Int32>) -> vmnet_return_t](./vmnet_read%28_,_,_%29.md)
  Attempts to read a specified number of packets from an interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_write(_:_:_:))*