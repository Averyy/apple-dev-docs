# net

**Framework**: Kernel

Access network-related utilities.

## Topics

### Address Resolution
- [inet_arp_handle_input](1584164-inet_arp_handle_input.md)
- [inet_arp_init_ifaddr](1584163-inet_arp_init_ifaddr.md)
- [inet_arp_lookup](1584165-inet_arp_lookup.md)
### bpf
- [bpf_attach](1589700-bpf_attach.md)
- [bpf_tap_in](1589470-bpf_tap_in.md)
- [bpf_tap_out](1589576-bpf_tap_out.md)
- [bpfattach](1589467-bpfattach.md)
### ether
- [ether_family_init](1397889-ether_family_init.md)
- [ether_add_proto](1397885-ether_add_proto.md)
- [ether_del_proto](1397887-ether_del_proto.md)
- [ether_demux](1397896-ether_demux.md)
- [ether_frameout](1397892-ether_frameout.md)
- [ether_ioctl](1397890-ether_ioctl.md)
- [ether_check_multi](1397894-ether_check_multi.md)
### ifnet
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
- [ifnet_stats_param](ifnet_stats_param.md)
- [ifnet_t](ifnet_t.md)

## See Also

- [architecture](architecture.md)
  Access machine-level and architectural information about the current platform.
- [bsm](bsm.md)
  Audit resource usage on the system.
- [hfs](hfs.md)
  Access HFS file-system data structures. 
- [kern](kern.md)
  Access kernel-level interfaces including clock, task, kernel extension, lock, and compression utilities.  
- [Math](math.md)
  Perform mathematical operations and manipulate integer, float, and double values.  
- [miscfs](miscfs.md)
  Access device nodes and other file-system entities.
- [Strings](strings.md)
  Compare, convert, and catenate strings and access the resulting content of those strings.
- [sys](sys.md)
  Access general system utilities for time, file systems, and system information.
- [vfs](vfs.md)
  Access the virtual file-system interfaces.
- [vm](vm.md)
  Interact with the virtual memory system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/net)*