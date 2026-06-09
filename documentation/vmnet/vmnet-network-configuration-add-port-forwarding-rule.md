# vmnet_network_configuration_add_port_forwarding_rule(_:_:_:_:_:_:)

**Framework**: vmnet  
**Kind**: func

Configures a new port forwarding rule for a vmnet network.

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_configuration_add_port_forwarding_rule(_ config: vmnet_network_configuration_ref, _ protocol: UInt8, _ address_family: sa_family_t, _ internal_port: UInt16, _ external_port: UInt16, _ internal_address: UnsafeRawPointer) -> vmnet_return_t
```

#### Return Value

`VMNET_SUCCESS` on success, an error otherwise.

#### Discussion

An app won’t be able to query or remove rules until the it starts the network. To do that, use [`vmnet_interface_remove_ip_port_forwarding_rule(_:_:_:_:_:)`](vmnet_interface_remove_ip_port_forwarding_rule(_:_:_:_:_:).md) or [`vmnet_interface_get_ip_port_forwarding_rules(_:_:_:)`](vmnet_interface_get_ip_port_forwarding_rules(_:_:_:).md) APIs, respectively.

## Parameters

- `config`: The network configuration object to modify.
- `protocol`: The protocol to apply the port forwarding rule to. Must be either `IPPROTO_TCP` or `IPPROTO_UDP` For more information,see the include file <netinet/in.h>.
- `address_family`: The address family (`AF_INET` or `AF_INET6`) of `internal_address`. If `AF_INET`, `internal address` must point to an `in_addr` structure. If `AF_INET6`, `internal_address` must point to a `in6_addr` structure.
- `internal_port`: The TCP or UDP port that the forwarded traffic should redirect to. Must be in host byte order.
- `external_port`: The TCP or UDP port on the outside network that the vmnet network should redirect from. This must be in host byte order.
- `internal_address`: Pointer to IPv4 or IPv6 address of the machine on the internal network that should receive the forwarded traffic.

## See Also

- [typealias vmnet_network_configuration_ref](vmnet_network_configuration_ref.md)
  A reference to a network vmnet network configuration.
- [func vmnet_network_configuration_add_dhcp_reservation(vmnet_network_configuration_ref, UnsafePointer<ether_addr_t>, UnsafePointer<in_addr>) -> vmnet_return_t](vmnet_network_configuration_add_dhcp_reservation(_:_:_:).md)
  Configures a new dhcp reservation for a vmnet network.
- [func vmnet_network_configuration_disable_router_advertisement(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_router_advertisement(_:).md)
  Disables router advertisement on a network.
- [func vmnet_network_configuration_disable_nat66(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_nat66(_:).md)
  Disables NAT66 on a network.
- [func vmnet_network_configuration_disable_nat44(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_nat44(_:).md)
  Disables NAT44 on a network.
- [func vmnet_network_configuration_disable_dns_proxy(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_dns_proxy(_:).md)
  Disables the DNS proxy on a network.
- [func vmnet_network_configuration_disable_dhcp(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_dhcp(_:).md)
  Disables DHCP server on a network.
- [let vmnet_nat66_prefix_length_key: UnsafePointer<CChar>](vmnet_nat66_prefix_length_key.md)
  The IPv6 prefix (uint64) to use with vmnet shared mode.
- [let vmnet_nat66_prefix_key: UnsafePointer<CChar>](vmnet_nat66_prefix_key.md)
  The IPv6 prefix string to use with vmnet shared mode.
- [func vmnet_port_forwarding_rule_get_details(xpc_object_t, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<in_addr>, UnsafeMutablePointer<UInt16>) -> vmnet_return_t](vmnet_port_forwarding_rule_get_details(_:_:_:_:_:).md)
  Extracts port forwarding rule details from the rule XPC dictionary object.
- [func vmnet_network_configuration_set_external_interface(vmnet_network_configuration_ref, UnsafePointer<CChar>) -> vmnet_return_t](vmnet_network_configuration_set_external_interface(_:_:).md)
  Configures the external interface of a vmnet network.
- [func vmnet_network_configuration_set_ipv4_subnet(vmnet_network_configuration_ref, UnsafePointer<in_addr>, UnsafePointer<in_addr>) -> vmnet_return_t](vmnet_network_configuration_set_ipv4_subnet(_:_:_:).md)
  Configures the IPv4 addresses of a vmnet network.
- [func vmnet_network_configuration_set_ipv6_prefix(vmnet_network_configuration_ref, UnsafePointer<in6_addr>, UInt8) -> vmnet_return_t](vmnet_network_configuration_set_ipv6_prefix(_:_:_:).md)
  Configures the IPv6 prefix for a vmnet network object.
- [func vmnet_network_configuration_set_mtu(vmnet_network_configuration_ref, UInt32) -> vmnet_return_t](vmnet_network_configuration_set_mtu(_:_:).md)
  Configures the maximum transmission unit (MTU) for a vmnet network.
- [func vmnet_network_get_ipv6_prefix(vmnet_network_ref, UnsafeMutablePointer<in6_addr>, UnsafeMutablePointer<UInt8>)](vmnet_network_get_ipv6_prefix(_:_:_:).md)
  Returns the IPv6 prefix of a network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_add_port_forwarding_rule(_:_:_:_:_:_:))*