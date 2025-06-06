# sock_send

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

## Declaration

```swift
errno_t sock_send(socket_t so, const struct msghdr *msg, int flags, size_t *sentlen);
```

#### Return_value

0 on success, EWOULDBLOCK if non-blocking and operation would cause the thread to block, otherwise the errno error.

#### Discussion

Send data on a socket. Similar to sendmsg. See 'man 2 sendmsg' for more information about sending data.

## Parameters

- `so`: The socket.
- `msg`: The msg describing how the data should be sent. Any pointers must point to data in the kernel.
- `flags`: See 'man 2 sendmsg'.
- `sentlen`: The number of bytes sent.

## See Also

- [sock_accept](1396149-sock_accept.md)
- [sock_bind](1396145-sock_bind.md)
- [sock_close](1396134-sock_close.md)
- [sock_connect](1396120-sock_connect.md)
- [sock_getpeername](1396137-sock_getpeername.md)
- [sock_getsockname](1396141-sock_getsockname.md)
- [sock_getsockopt](1396136-sock_getsockopt.md)
- [sock_gettype](1396147-sock_gettype.md)
- [sock_inject_data_in](1433192-sock_inject_data_in.md)
- [sock_inject_data_out](1433162-sock_inject_data_out.md)
- [sock_ioctl](1396118-sock_ioctl.md)
- [sock_isconnected](1396130-sock_isconnected.md)
- [sock_isnonblocking](1396116-sock_isnonblocking.md)
- [sock_listen](1396139-sock_listen.md)
- [sock_receive](1396126-sock_receive.md)
- [sock_receivembuf](1396114-sock_receivembuf.md)
- [sock_sendmbuf](1396128-sock_sendmbuf.md)
- [sock_setpriv](1396124-sock_setpriv.md)
- [sock_setsockopt](1396148-sock_setsockopt.md)
- [sock_shutdown](1396150-sock_shutdown.md)
- [sock_socket](1396122-sock_socket.md)
- [sockopt_copyin](1433166-sockopt_copyin.md)
- [sockopt_copyout](1433176-sockopt_copyout.md)
- [sockopt_direction](1433253-sockopt_direction.md)
- [sockopt_level](1433193-sockopt_level.md)
- [sockopt_name](1433249-sockopt_name.md)
- [sockopt_valsize](1433272-sockopt_valsize.md)
- [ifaddr_address](1525073-ifaddr_address.md)
- [ifaddr_address_family](1524915-ifaddr_address_family.md)
- [ifaddr_dstaddress](1525058-ifaddr_dstaddress.md)
- [ifaddr_findbestforaddr](1525009-ifaddr_findbestforaddr.md)
- [ifaddr_ifnet](1524949-ifaddr_ifnet.md)
- [ifaddr_netmask](1525132-ifaddr_netmask.md)
- [ifaddr_reference](1525060-ifaddr_reference.md)
- [ifaddr_release](1524928-ifaddr_release.md)
- [ifaddr_withaddr](1524859-ifaddr_withaddr.md)
- [ifaddr_withdstaddr](1525107-ifaddr_withdstaddr.md)
- [ifaddr_withnet](1524842-ifaddr_withnet.md)
- [ifaddr_withroute](1524963-ifaddr_withroute.md)
- [iflt_attach](1589956-iflt_attach.md)
- [iflt_detach](1589950-iflt_detach.md)
- [ifmaddr_address](1524853-ifmaddr_address.md)
- [ifmaddr_ifnet](1525101-ifmaddr_ifnet.md)
- [ifmaddr_lladdress](1525091-ifmaddr_lladdress.md)
- [ifmaddr_reference](1524890-ifmaddr_reference.md)
- [ifmaddr_release](1525024-ifmaddr_release.md)
- [ifnet_add_multicast](1524976-ifnet_add_multicast.md)
- [ifnet_addrlen](1524855-ifnet_addrlen.md)
- [ifnet_allocate](1525028-ifnet_allocate.md)
- [ifnet_attach](1524922-ifnet_attach.md)
- [ifnet_attach_protocol](1525004-ifnet_attach_protocol.md)
- [ifnet_attach_protocol_v2](1525131-ifnet_attach_protocol_v2.md)
- [ifnet_baudrate](1524866-ifnet_baudrate.md)
- [ifnet_capabilities_enabled](1525016-ifnet_capabilities_enabled.md)
- [ifnet_capabilities_supported](1524931-ifnet_capabilities_supported.md)
- [ifnet_detach](1524903-ifnet_detach.md)
- [ifnet_detach_protocol](1525007-ifnet_detach_protocol.md)
- [ifnet_event](1524986-ifnet_event.md)
- [ifnet_family](1524921-ifnet_family.md)
- [ifnet_find_by_name](1525072-ifnet_find_by_name.md)
- [ifnet_flags](1525111-ifnet_flags.md)
- [ifnet_free_address_list](1524991-ifnet_free_address_list.md)
- [ifnet_free_multicast_list](1524898-ifnet_free_multicast_list.md)
- [ifnet_get_address_list](1525146-ifnet_get_address_list.md)
- [ifnet_get_address_list_family](1525142-ifnet_get_address_list_family.md)
- [ifnet_get_link_mib_data](1524988-ifnet_get_link_mib_data.md)
- [ifnet_get_link_mib_data_length](1524864-ifnet_get_link_mib_data_length.md)
- [ifnet_get_multicast_list](1525020-ifnet_get_multicast_list.md)
- [ifnet_get_tso_mtu](1524965-ifnet_get_tso_mtu.md)
- [ifnet_get_wake_flags](1524907-ifnet_get_wake_flags.md)
- [ifnet_hdrlen](1524895-ifnet_hdrlen.md)
- [ifnet_index](1525041-ifnet_index.md)
- [ifnet_input](1525087-ifnet_input.md)
- [ifnet_interface_family_find](1524844-ifnet_interface_family_find.md)
- [ifnet_ioctl](1525082-ifnet_ioctl.md)
- [ifnet_lastchange](1525140-ifnet_lastchange.md)
- [ifnet_list_free](1524868-ifnet_list_free.md)
- [ifnet_list_get](1524913-ifnet_list_get.md)
- [ifnet_lladdr_copy_bytes](1525069-ifnet_lladdr_copy_bytes.md)
- [ifnet_llbroadcast_copy_bytes](1525030-ifnet_llbroadcast_copy_bytes.md)
- [ifnet_metric](1524964-ifnet_metric.md)
- [ifnet_mtu](1524959-ifnet_mtu.md)
- [ifnet_name](1524885-ifnet_name.md)
- [ifnet_offload](1524854-ifnet_offload.md)
- [ifnet_output](1525046-ifnet_output.md)
- [ifnet_output_raw](1525049-ifnet_output_raw.md)
- [ifnet_reference](1524857-ifnet_reference.md)
- [ifnet_release](1525052-ifnet_release.md)
- [ifnet_remove_multicast](1524982-ifnet_remove_multicast.md)
- [ifnet_resolve_multicast](1525080-ifnet_resolve_multicast.md)
- [ifnet_set_addrlen](1524861-ifnet_set_addrlen.md)
- [ifnet_set_baudrate](1525090-ifnet_set_baudrate.md)
- [ifnet_set_capabilities_enabled](1524938-ifnet_set_capabilities_enabled.md)
- [ifnet_set_capabilities_supported](1525144-ifnet_set_capabilities_supported.md)
- [ifnet_set_flags](1524996-ifnet_set_flags.md)
- [ifnet_set_hdrlen](1525097-ifnet_set_hdrlen.md)
- [ifnet_set_link_mib_data](1525120-ifnet_set_link_mib_data.md)
- [ifnet_set_lladdr](1524891-ifnet_set_lladdr.md)
- [ifnet_set_metric](1524932-ifnet_set_metric.md)
- [ifnet_set_mtu](1524919-ifnet_set_mtu.md)
- [ifnet_set_offload](1524961-ifnet_set_offload.md)
- [ifnet_set_promiscuous](1524973-ifnet_set_promiscuous.md)
- [ifnet_set_stat](1524994-ifnet_set_stat.md)
- [ifnet_set_tso_mtu](1525098-ifnet_set_tso_mtu.md)
- [ifnet_set_wake_flags](1525070-ifnet_set_wake_flags.md)
- [ifnet_softc](1524952-ifnet_softc.md)
- [ifnet_stat](1525068-ifnet_stat.md)
- [ifnet_stat_increment](1525065-ifnet_stat_increment.md)
- [ifnet_stat_increment_in](1525002-ifnet_stat_increment_in.md)
- [ifnet_stat_increment_out](1525085-ifnet_stat_increment_out.md)
- [ifnet_touch_lastchange](1524957-ifnet_touch_lastchange.md)
- [ifnet_type](1524954-ifnet_type.md)
- [ifnet_unit](1525055-ifnet_unit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1396143-sock_send)*