# ifnet_add_proto_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*ifnet_add_proto_func)(ifnet_t interface, protocol_family_t protocol_family, const struct ifnet_demux_desc *demux_array, u_int32_t demux_count);
```

#### Return_value

If the result is zero, processing will continue normally. If the result is anything else, the add protocol will be aborted.

#### Discussion

if_add_proto_func is called by the stack when a protocol is attached to an interface. This gives the interface an opportunity to get a list of protocol description structures for demuxing packets to this protocol (demux descriptors).

## Parameters

- `interface`: The interface the protocol will be attached to.
- `protocol_family`: The family of the protocol being attached.
- `demux_array`: An array of demux descriptors that describe the interface specific ways of identifying packets belonging to this protocol family.
- `demux_count`: The number of demux descriptors in the array.

## See Also

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
- [ifnet_stats_param](ifnet_stats_param.md)
- [ifnet_t](ifnet_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_add_proto_func)*