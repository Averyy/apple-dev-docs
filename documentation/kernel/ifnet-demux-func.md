# ifnet_demux_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*ifnet_demux_func)(ifnet_t interface, mbuf_t packet, char *frame_header, protocol_family_t *protocol_family);
```

#### Return_value

If the result is zero, processing will continue normally. If the result is EJUSTRETURN, processing will stop but the packet will not be freed. If the result is anything else, the processing will stop and the packet will be freed.

#### Discussion

ifnet_demux_func is called for each inbound packet to determine which protocol family the packet belongs to. This information is then used by the stack to determine which protocol to pass the packet to. This function may return protocol families for protocols that are not attached. If the protocol family has not been attached to the interface, the packet will be discarded.

## Parameters

- `interface`: The interface the packet was received on.
- `packet`: The mbuf containing the packet.
- `frame_header`: A pointer to the frame header.
- `protocol_family`: Upon return, the protocol family matching the packet should be stored here.

## See Also

- [ifnet_add_proto_func](ifnet_add_proto_func.md)
- [ifnet_attach_proto_param](ifnet_attach_proto_param.md)
- [ifnet_attach_proto_param_v2](ifnet_attach_proto_param_v2.md)
- [ifnet_check_multi](ifnet_check_multi.md)
- [ifnet_del_proto_func](ifnet_del_proto_func.md)
- [ifnet_demux_desc](ifnet_demux_desc.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_demux_func)*