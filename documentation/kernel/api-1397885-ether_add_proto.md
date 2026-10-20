# ether_add_proto

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
errno_t ether_add_proto(ifnet_t interface, protocol_family_t protocol, const struct ifnet_demux_desc *demux_list, u_int32_t demux_count);
```

## See Also

### ether
- [ether_family_init](./api-1397889-ether_family_init.md)
- [ether_del_proto](./api-1397887-ether_del_proto.md)
- [ether_demux](./api-1397896-ether_demux.md)
- [ether_frameout](./api-1397892-ether_frameout.md)
- [ether_ioctl](./api-1397890-ether_ioctl.md)
- [ether_check_multi](./api-1397894-ether_check_multi.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1397885-ether_add_proto)*