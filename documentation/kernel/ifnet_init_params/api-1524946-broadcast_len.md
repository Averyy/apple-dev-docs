# broadcast_len

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The length of the link-layer broadcast address.

**Availability**:
- macOS 10.6+

## Declaration

```c
u_int32_t broadcast_len;
```

## See Also

### Fields
- [uniqueid](./api-1524929-uniqueid.md)
  An identifier unique to this instance of the interface.
- [uniqueid_len](./api-1524998-uniqueid_len.md)
  The length, in bytes, of the uniqueid.
- [name](./api-1525014-name.md)
  The interface name (i.e. en).
- [unit](./api-1525129-unit.md)
  The interface unit number (en0's unit number is 0).
- [family](./api-1525032-family.md)
  The interface family.
- [type](./api-1525100-type.md)
  The interface type (see sys/if_types.h). Must be less than 256. For new types, use IFT_OTHER.
- [output](./api-1525122-output.md)
  The output function for the interface. Every packet the stack attempts to send through this interface will go out through this function.
- [demux](./api-1524941-demux.md)
  The function used to determine the protocol family of an incoming packet.
- [add_proto](./api-1524940-add_proto.md)
  The function used to attach a protocol to this interface.
- [del_proto](./api-1525067-del_proto.md)
  The function used to remove a protocol from this interface.
- [framer](./api-1525115-framer.md)
  The function used to frame outbound packets, may be NULL.
- [softc](./api-1525064-softc.md)
  Driver specific storage. This value can be retrieved from the ifnet using the ifnet_softc function.
- [ioctl](./api-1525015-ioctl.md)
  The function used to handle ioctls.
- [set_bpf_tap](./api-1524876-set_bpf_tap.md)
  The function used to set the bpf_tap function.
- [detach](./api-1524897-detach.md)
  The function called to let the driver know the interface has been detached.
- [event](./api-1525117-event.md)
  The function to notify the interface of various interface specific kernel events.
- [broadcast_addr](./api-1524918-broadcast_addr.md)
  The link-layer broadcast address for this interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_init_params/1524946-broadcast_len)*