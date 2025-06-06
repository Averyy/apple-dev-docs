# ifnet_ioctl_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*ifnet_ioctl_func)(ifnet_t interface, unsigned long cmd, void *data);
```

#### Discussion

ifnet_ioctl_func is used to communicate ioctls from the stack to the driver.

All undefined ioctls are reserved for future use by Apple. If you need to communicate with your kext using an ioctl, please use SIOCSIFKPI and SIOCGIFKPI.

## Parameters

- `interface`: The interface the ioctl is being sent to.
- `proto_family`: The protocol family to handle the ioctl, may be zero for no protocol_family.
- `cmd`: The ioctl command.
- `data`: A pointer to any data related to the ioctl.

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
- [ifnet_offload_t](ifnet_offload_t.md)
  Flags indicating the offload support of the interface.
- [ifnet_output_func](ifnet_output_func.md)
- [ifnet_set_bpf_tap](ifnet_set_bpf_tap.md)
- [ifnet_stat_increment_param](ifnet_stat_increment_param.md)
- [ifnet_stats_param](ifnet_stats_param.md)
- [ifnet_t](ifnet_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_ioctl_func)*