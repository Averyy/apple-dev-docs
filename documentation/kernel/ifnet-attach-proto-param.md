# ifnet_attach_proto_param

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct ifnet_attach_proto_param {
    ...
};
```

#### Discussion

This structure is used to attach a protocol to an interface. This structure provides the various functions for handling operations related to the protocol on the interface as well as information for how to demux packets for this protocol.

## Topics

### Fields
- [demux_array](ifnet_attach_proto_param/1525038-demux_array.md)
  An array of ifnet_demux_desc structures describing the protocol.
- [demux_count](ifnet_attach_proto_param/1525033-demux_count.md)
  The number of entries in the demux_array array.
- [input](ifnet_attach_proto_param/1524849-input.md)
  The function to be called for inbound packets.
- [pre_output](ifnet_attach_proto_param/1524845-pre_output.md)
  The function to be called for outbound packets.
- [event](ifnet_attach_proto_param/1524843-event.md)
  The function to be called for interface events.
- [ioctl](ifnet_attach_proto_param/1525050-ioctl.md)
  The function to be called for ioctls.
- [detached](ifnet_attach_proto_param/1524863-detached.md)
  The function to be called for handling the detach.
### Instance Properties
- [resolve](ifnet_attach_proto_param/1525021-resolve.md)
- [send_arp](ifnet_attach_proto_param/1525056-send_arp.md)

## See Also

- [ifnet_add_proto_func](ifnet_add_proto_func.md)
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
- [ifnet_init_params](ifnet_init_params.md)
- [ifnet_ioctl_func](ifnet_ioctl_func.md)
- [ifnet_offload_t](ifnet_offload_t.md)
  Flags indicating the offload support of the interface.
- [ifnet_output_func](ifnet_output_func.md)
- [ifnet_set_bpf_tap](ifnet_set_bpf_tap.md)
- [ifnet_stat_increment_param](ifnet_stat_increment_param.md)
- [ifnet_stats_param](ifnet_stats_param.md)
- [ifnet_t](ifnet_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_attach_proto_param)*