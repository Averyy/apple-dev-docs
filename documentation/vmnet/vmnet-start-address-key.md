# vmnet_start_address_key

**Framework**: vmnet  
**Kind**: var

A string that represents th starting IPv4 address to use for the interface.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
let vmnet_start_address_key: UnsafePointer<CChar>
```

#### Discussion

This address to use as the gateway address. The framework places subsequent address up to and including `vmnet_end_address_key` in the DHCP pool. All other addresses are available for static assignment. The address needs to meet the folloowing requirements:

- The address must be in the private IP range (RFC 1918).
- You must specify this along with `vmnet_end_address_key` and `vmnet_subnet_mask_key`.
- It may be present in the `interface_desc` and `interface_param` dictionaries.

## See Also

- [let vmnet_allocate_mac_address_key: UnsafePointer<CChar>](vmnet_allocate_mac_address_key.md)
- [let vmnet_enable_checksum_offload_key: UnsafePointer<CChar>](vmnet_enable_checksum_offload_key.md)
- [let vmnet_enable_isolation_key: UnsafePointer<CChar>](vmnet_enable_isolation_key.md)
- [let vmnet_enable_tso_key: UnsafePointer<CChar>](vmnet_enable_tso_key.md)
- [let vmnet_end_address_key: UnsafePointer<CChar>](vmnet_end_address_key.md)
- [let vmnet_host_ip_address_key: UnsafePointer<CChar>](vmnet_host_ip_address_key.md)
- [let vmnet_host_ipv6_address_key: UnsafePointer<CChar>](vmnet_host_ipv6_address_key.md)
- [let vmnet_host_subnet_mask_key: UnsafePointer<CChar>](vmnet_host_subnet_mask_key.md)
- [let vmnet_nat66_prefix_key: UnsafePointer<CChar>](vmnet_nat66_prefix_key.md)
  The IPv6 prefix string to use with vmnet shared mode.
- [let vmnet_nat66_prefix_length_key: UnsafePointer<CChar>](vmnet_nat66_prefix_length_key.md)
  The IPv6 prefix (uint64) to use with vmnet shared mode.
- [let vmnet_network_identifier_key: UnsafePointer<CChar>](vmnet_network_identifier_key.md)
  The identifier that uniquely identifies this network as a UUID.
- [let vmnet_read_max_packets_key: UnsafePointer<CChar>](vmnet_read_max_packets_key.md)
- [let vmnet_shared_interface_name_key: UnsafePointer<CChar>](vmnet_shared_interface_name_key.md)
  A string that represents the name of the interface to use when the operating mode of the interface in the vmnet bridged mode.
- [let vmnet_subnet_mask_key: UnsafePointer<CChar>](vmnet_subnet_mask_key.md)
  A string that represnts the IPv4 subnet mask to use on the interface.
- [let vmnet_operation_mode_key: UnsafePointer<CChar>](vmnet_operation_mode_key.md)
  The mode to use to configure the guest operating system network interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_start_address_key)*