# ifnet_init_params

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct ifnet_init_params {
    ...
};
```

#### Discussion

This structure is used to define various properties of the interface when calling ifnet_allocate. A copy of these values will be stored in the ifnet and cannot be modified while the interface is attached.

## Topics

### Fields
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
- [broadcast_addr](ifnet_init_params/1524918-broadcast_addr.md)
  The link-layer broadcast address for this interface.
- [broadcast_len](ifnet_init_params/1524946-broadcast_len.md)
  The length of the link-layer broadcast address.
### Instance Properties
- [check_multi](ifnet_init_params/1524969-check_multi.md)

## See Also

- [ifnet_add_proto_func](ifnet_add_proto_func.md)
- [ifnet_attach_proto_param](ifnet_attach_proto_param.md)
- [ifnet_attach_proto_param_v2](ifnet_attach_proto_param_v2.md)
- [ifnet_check_multi](ifnet_check_multi.md)
- [ifnet_del_proto_func](ifnet_del_proto_func.md)
- [ifnet_demux_desc](ifnet_demux_desc.md)
- [ifnet_demux_func](ifnet_demux_func.md)
- [ifnet_detached_func](ifnet_detached_func.md)
- [ifnet_event_func](ifnet_event_func.md)
- [ifnet_family_t](ifnet_family_t.md)
  Storage type for the interface family.
- [ifnet_framer_func](ifnet_framer_func.md)
- [ifnet_ioctl_func](ifnet_ioctl_func.md)
- [ifnet_offload_t](ifnet_offload_t.md)
  Flags indicating the offload support of the interface.
- [ifnet_output_func](ifnet_output_func.md)
- [ifnet_set_bpf_tap](ifnet_set_bpf_tap.md)
- [ifnet_stat_increment_param](ifnet_stat_increment_param.md)
- [ifnet_stats_param](ifnet_stats_param.md)
- [ifnet_t](ifnet_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_init_params)*