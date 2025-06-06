# ifnet_set_bpf_tap

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*ifnet_set_bpf_tap)(ifnet_t interface, bpf_tap_mode mode, bpf_packet_func callback);
```

#### Discussion

Deprecated. Specify NULL. Call bpf_tap_in/bpf_tap_out for all packets.

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
- [ifnet_stat_increment_param](ifnet_stat_increment_param.md)
- [ifnet_stats_param](ifnet_stats_param.md)
- [ifnet_t](ifnet_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_set_bpf_tap)*