# broadcast_addr

**Framework**: Kernel  
**Kind**: structp

The link-layer broadcast address for this interface.

**Availability**:
- macOS 10.6+

## Declaration

```swift
const void *broadcast_addr;
```

## See Also

- [uniqueid](ifnet_init_params/1524929-uniqueid.md)
  An identifier unique to this instance of the interface.
- [uniqueid_len](ifnet_init_params/1524998-uniqueid_len.md)
  The length, in bytes, of the uniqueid.
- [name](ifnet_init_params/1525014-name.md)
  The interface name (i.e. en).
- [unit](ifnet_init_params/1525129-unit.md)
  The interface unit number (en0's unit number is 0).
- [family](ifnet_init_params/1525032-family.md)
  The interface family.
- [type](ifnet_init_params/1525100-type.md)
  The interface type (see sys/if_types.h). Must be less than 256. For new types, use IFT_OTHER.
- [output](ifnet_init_params/1525122-output.md)
  The output function for the interface. Every packet the stack attempts to send through this interface will go out through this function.
- [demux](ifnet_init_params/1524941-demux.md)
  The function used to determine the protocol family of an incoming packet.
- [add_proto](ifnet_init_params/1524940-add_proto.md)
  The function used to attach a protocol to this interface.
- [del_proto](ifnet_init_params/1525067-del_proto.md)
  The function used to remove a protocol from this interface.
- [framer](ifnet_init_params/1525115-framer.md)
  The function used to frame outbound packets, may be NULL.
- [softc](ifnet_init_params/1525064-softc.md)
  Driver specific storage. This value can be retrieved from the ifnet using the ifnet_softc function.
- [ioctl](ifnet_init_params/1525015-ioctl.md)
  The function used to handle ioctls.
- [set_bpf_tap](ifnet_init_params/1524876-set_bpf_tap.md)
  The function used to set the bpf_tap function.
- [detach](ifnet_init_params/1524897-detach.md)
  The function called to let the driver know the interface has been detached.
- [event](ifnet_init_params/1525117-event.md)
  The function to notify the interface of various interface specific kernel events.
- [broadcast_len](ifnet_init_params/1524946-broadcast_len.md)
  The length of the link-layer broadcast address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_init_params/1524918-broadcast_addr)*