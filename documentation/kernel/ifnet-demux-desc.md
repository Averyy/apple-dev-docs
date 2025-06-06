# ifnet_demux_desc

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct ifnet_demux_desc {
    ...
};
```

#### Discussion

This structure is to identify packets that belong to a specific protocol. The types supported are interface specific. Ethernet supports ETHER_DESC_ETYPE2, ETHER_DESC_SAP, and ETHER_DESC_SNAP. The type defines the offset in the packet where the data will be matched as well as context. For example, if ETHER_DESC_SNAP is specified, the only valid datalen is 5 and only in the 5 bytes will only be matched when the packet header indicates that the packet is a SNAP packet.

## Topics

### Fields
- [type](ifnet_demux_desc/1524955-type.md)
  The type of identifier data (i.e. ETHER_DESC_ETYPE2)
- [data](ifnet_demux_desc/1524905-data.md)
  A pointer to an entry of type (i.e. pointer to 0x0800).
- [datalen](ifnet_demux_desc/1524926-datalen.md)
  The number of bytes of data used to describe the packet.

## See Also

- [ifnet_add_proto_func](ifnet_add_proto_func.md)
- [ifnet_attach_proto_param](ifnet_attach_proto_param.md)
- [ifnet_attach_proto_param_v2](ifnet_attach_proto_param_v2.md)
- [ifnet_check_multi](ifnet_check_multi.md)
- [ifnet_del_proto_func](ifnet_del_proto_func.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_demux_desc)*