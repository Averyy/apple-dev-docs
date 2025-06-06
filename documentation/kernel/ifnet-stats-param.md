# ifnet_stats_param

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct ifnet_stats_param {
    ...
};
```

#### Discussion

This structure is used get and set the interface statistics.

## Topics

### Fields
- [packets_in](ifnet_stats_param/1524989-packets_in.md)
  The number of packets received.
- [bytes_in](ifnet_stats_param/1524883-bytes_in.md)
  The number of bytes received.
- [errors_in](ifnet_stats_param/1524933-errors_in.md)
  The number of receive errors.
- [packets_out](ifnet_stats_param/1525128-packets_out.md)
  The number of packets transmitted.
- [bytes_out](ifnet_stats_param/1525110-bytes_out.md)
  The number of bytes transmitted.
- [errors_out](ifnet_stats_param/1524902-errors_out.md)
  The number of transmission errors.
- [collisions](ifnet_stats_param/1525096-collisions.md)
  The number of collisions seen by this interface.
- [dropped](ifnet_stats_param/1525094-dropped.md)
  The number of packets dropped.
### Instance Properties
- [multicasts_in](ifnet_stats_param/1525042-multicasts_in.md)
- [multicasts_out](ifnet_stats_param/1525036-multicasts_out.md)
- [no_protocol](ifnet_stats_param/1525124-no_protocol.md)

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
- [ifnet_init_params](ifnet_init_params.md)
- [ifnet_ioctl_func](ifnet_ioctl_func.md)
- [ifnet_offload_t](ifnet_offload_t.md)
  Flags indicating the offload support of the interface.
- [ifnet_output_func](ifnet_output_func.md)
- [ifnet_set_bpf_tap](ifnet_set_bpf_tap.md)
- [ifnet_stat_increment_param](ifnet_stat_increment_param.md)
- [ifnet_t](ifnet_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_stats_param)*