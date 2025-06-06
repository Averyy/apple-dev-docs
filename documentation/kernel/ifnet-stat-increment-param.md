# ifnet_stat_increment_param

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct ifnet_stat_increment_param {
    ...
};
```

#### Discussion

This structure is used increment the counters on a network interface.

## Topics

### Fields
- [packets_in](ifnet_stat_increment_param/1525109-packets_in.md)
  The number of packets received.
- [bytes_in](ifnet_stat_increment_param/1525011-bytes_in.md)
  The number of bytes received.
- [errors_in](ifnet_stat_increment_param/1525113-errors_in.md)
  The number of receive errors.
- [packets_out](ifnet_stat_increment_param/1525136-packets_out.md)
  The number of packets transmitted.
- [bytes_out](ifnet_stat_increment_param/1524877-bytes_out.md)
  The number of bytes transmitted.
- [errors_out](ifnet_stat_increment_param/1524993-errors_out.md)
  The number of transmission errors.
- [collisions](ifnet_stat_increment_param/1524975-collisions.md)
  The number of collisions seen by this interface.
- [dropped](ifnet_stat_increment_param/1525040-dropped.md)
  The number of packets dropped.

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
- [ifnet_stats_param](ifnet_stats_param.md)
- [ifnet_t](ifnet_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_stat_increment_param)*