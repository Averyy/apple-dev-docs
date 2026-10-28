# sockopt_name

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

## Declaration

```c
int sockopt_name(sockopt_t sopt);
```

## Return Value

The socket option name. See man 2 setsockopt

## Discussion

Retrieves the socket option name. (SO_SNDBUF, etc).

## Parameters

- `sopt`: The socket option.

## See Also

### Network Kernel Extensions
- [sock_accept](./api-1396149-sock_accept.md)
- [sock_bind](./api-1396145-sock_bind.md)
- [sock_close](./api-1396134-sock_close.md)
- [sock_connect](./api-1396120-sock_connect.md)
- [sock_getpeername](./api-1396137-sock_getpeername.md)
- [sock_getsockname](./api-1396141-sock_getsockname.md)
- [sock_getsockopt](./api-1396136-sock_getsockopt.md)
- [sock_gettype](./api-1396147-sock_gettype.md)
- [sock_inject_data_in](./api-1433192-sock_inject_data_in.md)
- [sock_inject_data_out](./api-1433162-sock_inject_data_out.md)
- [sock_ioctl](./api-1396118-sock_ioctl.md)
- [sock_isconnected](./api-1396130-sock_isconnected.md)
- [sock_isnonblocking](./api-1396116-sock_isnonblocking.md)
- [sock_listen](./api-1396139-sock_listen.md)
- [sock_receive](./api-1396126-sock_receive.md)
- [sock_receivembuf](./api-1396114-sock_receivembuf.md)
- [sock_send](./api-1396143-sock_send.md)
- [sock_sendmbuf](./api-1396128-sock_sendmbuf.md)
- [sock_setpriv](./api-1396124-sock_setpriv.md)
- [sock_setsockopt](./api-1396148-sock_setsockopt.md)
- [sock_shutdown](./api-1396150-sock_shutdown.md)
- [sock_socket](./api-1396122-sock_socket.md)
- [sockopt_copyin](./api-1433166-sockopt_copyin.md)
- [sockopt_copyout](./api-1433176-sockopt_copyout.md)
- [sockopt_direction](./api-1433253-sockopt_direction.md)
- [sockopt_level](./api-1433193-sockopt_level.md)
- [sockopt_valsize](./api-1433272-sockopt_valsize.md)
- [ifaddr_address](./api-1525073-ifaddr_address.md)
- [ifaddr_address_family](./api-1524915-ifaddr_address_family.md)
- [ifaddr_dstaddress](./api-1525058-ifaddr_dstaddress.md)
- [ifaddr_findbestforaddr](./api-1525009-ifaddr_findbestforaddr.md)
- [ifaddr_ifnet](./api-1524949-ifaddr_ifnet.md)
- [ifaddr_netmask](./api-1525132-ifaddr_netmask.md)
- [ifaddr_reference](./api-1525060-ifaddr_reference.md)
- [ifaddr_release](./api-1524928-ifaddr_release.md)
- [ifaddr_withaddr](./api-1524859-ifaddr_withaddr.md)
- [ifaddr_withdstaddr](./api-1525107-ifaddr_withdstaddr.md)
- [ifaddr_withnet](./api-1524842-ifaddr_withnet.md)
- [ifaddr_withroute](./api-1524963-ifaddr_withroute.md)
- [iflt_attach](./api-1589956-iflt_attach.md)
- [iflt_detach](./api-1589950-iflt_detach.md)
- [ifmaddr_address](./api-1524853-ifmaddr_address.md)
- [ifmaddr_ifnet](./api-1525101-ifmaddr_ifnet.md)
- [ifmaddr_lladdress](./api-1525091-ifmaddr_lladdress.md)
- [ifmaddr_reference](./api-1524890-ifmaddr_reference.md)
- [ifmaddr_release](./api-1525024-ifmaddr_release.md)
- [ifnet_add_multicast](./api-1524976-ifnet_add_multicast.md)
- [ifnet_addrlen](./api-1524855-ifnet_addrlen.md)
- [ifnet_allocate](./api-1525028-ifnet_allocate.md)
- [ifnet_attach](./api-1524922-ifnet_attach.md)
- [ifnet_attach_protocol](./api-1525004-ifnet_attach_protocol.md)
- [ifnet_attach_protocol_v2](./api-1525131-ifnet_attach_protocol_v2.md)
- [ifnet_baudrate](./api-1524866-ifnet_baudrate.md)
- [ifnet_capabilities_enabled](./api-1525016-ifnet_capabilities_enabled.md)
- [ifnet_capabilities_supported](./api-1524931-ifnet_capabilities_supported.md)
- [ifnet_detach](./api-1524903-ifnet_detach.md)
- [ifnet_detach_protocol](./api-1525007-ifnet_detach_protocol.md)
- [ifnet_event](./api-1524986-ifnet_event.md)
- [ifnet_family](./api-1524921-ifnet_family.md)
- [ifnet_find_by_name](./api-1525072-ifnet_find_by_name.md)
- [ifnet_flags](./api-1525111-ifnet_flags.md)
- [ifnet_free_address_list](./api-1524991-ifnet_free_address_list.md)
- [ifnet_free_multicast_list](./api-1524898-ifnet_free_multicast_list.md)
- [ifnet_get_address_list](./api-1525146-ifnet_get_address_list.md)
- [ifnet_get_address_list_family](./api-1525142-ifnet_get_address_list_family.md)
- [ifnet_get_link_mib_data](./api-1524988-ifnet_get_link_mib_data.md)
- [ifnet_get_link_mib_data_length](./api-1524864-ifnet_get_link_mib_data_length.md)
- [ifnet_get_multicast_list](./api-1525020-ifnet_get_multicast_list.md)
- [ifnet_get_tso_mtu](./api-1524965-ifnet_get_tso_mtu.md)
- [ifnet_get_wake_flags](./api-1524907-ifnet_get_wake_flags.md)
- [ifnet_hdrlen](./api-1524895-ifnet_hdrlen.md)
- [ifnet_index](./api-1525041-ifnet_index.md)
- [ifnet_input](./api-1525087-ifnet_input.md)
- [ifnet_interface_family_find](./api-1524844-ifnet_interface_family_find.md)
- [ifnet_ioctl](./api-1525082-ifnet_ioctl.md)
- [ifnet_lastchange](./api-1525140-ifnet_lastchange.md)
- [ifnet_list_free](./api-1524868-ifnet_list_free.md)
- [ifnet_list_get](./api-1524913-ifnet_list_get.md)
- [ifnet_lladdr_copy_bytes](./api-1525069-ifnet_lladdr_copy_bytes.md)
- [ifnet_llbroadcast_copy_bytes](./api-1525030-ifnet_llbroadcast_copy_bytes.md)
- [ifnet_metric](./api-1524964-ifnet_metric.md)
- [ifnet_mtu](./api-1524959-ifnet_mtu.md)
- [ifnet_name](./api-1524885-ifnet_name.md)
- [ifnet_offload](./api-1524854-ifnet_offload.md)
- [ifnet_output](./api-1525046-ifnet_output.md)
- [ifnet_output_raw](./api-1525049-ifnet_output_raw.md)
- [ifnet_reference](./api-1524857-ifnet_reference.md)
- [ifnet_release](./api-1525052-ifnet_release.md)
- [ifnet_remove_multicast](./api-1524982-ifnet_remove_multicast.md)
- [ifnet_resolve_multicast](./api-1525080-ifnet_resolve_multicast.md)
- [ifnet_set_addrlen](./api-1524861-ifnet_set_addrlen.md)
- [ifnet_set_baudrate](./api-1525090-ifnet_set_baudrate.md)
- [ifnet_set_capabilities_enabled](./api-1524938-ifnet_set_capabilities_enabled.md)
- [ifnet_set_capabilities_supported](./api-1525144-ifnet_set_capabilities_supported.md)
- [ifnet_set_flags](./api-1524996-ifnet_set_flags.md)
- [ifnet_set_hdrlen](./api-1525097-ifnet_set_hdrlen.md)
- [ifnet_set_link_mib_data](./api-1525120-ifnet_set_link_mib_data.md)
- [ifnet_set_lladdr](./api-1524891-ifnet_set_lladdr.md)
- [ifnet_set_metric](./api-1524932-ifnet_set_metric.md)
- [ifnet_set_mtu](./api-1524919-ifnet_set_mtu.md)
- [ifnet_set_offload](./api-1524961-ifnet_set_offload.md)
- [ifnet_set_promiscuous](./api-1524973-ifnet_set_promiscuous.md)
- [ifnet_set_stat](./api-1524994-ifnet_set_stat.md)
- [ifnet_set_tso_mtu](./api-1525098-ifnet_set_tso_mtu.md)
- [ifnet_set_wake_flags](./api-1525070-ifnet_set_wake_flags.md)
- [ifnet_softc](./api-1524952-ifnet_softc.md)
- [ifnet_stat](./api-1525068-ifnet_stat.md)
- [ifnet_stat_increment](./api-1525065-ifnet_stat_increment.md)
- [ifnet_stat_increment_in](./api-1525002-ifnet_stat_increment_in.md)
- [ifnet_stat_increment_out](./api-1525085-ifnet_stat_increment_out.md)
- [ifnet_touch_lastchange](./api-1524957-ifnet_touch_lastchange.md)
- [ifnet_type](./api-1524954-ifnet_type.md)
- [ifnet_unit](./api-1525055-ifnet_unit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1433249-sockopt_name)*