# vmnet_network_configuration_disable_dns_proxy(_:)

**Framework**: vmnet  
**Kind**: func

Disables the DNS proxy on a network.

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_configuration_disable_dns_proxy(_ config: vmnet_network_configuration_ref)
```

## Parameters

- `config`: The network configuration object for the framework to modify.

## See Also

- [typealias vmnet_network_configuration_ref](vmnet_network_configuration_ref.md)
  A reference to a network vmnet network configuration.
- [func vmnet_network_configuration_add_dhcp_reservation(vmnet_network_configuration_ref, UnsafePointer<ether_addr_t>, UnsafePointer<in_addr>) -> vmnet_return_t](vmnet_network_configuration_add_dhcp_reservation(_:_:_:).md)
  Configures a new dhcp reservation for a vmnet network.
- [func vmnet_network_configuration_add_port_forwarding_rule(vmnet_network_configuration_ref, UInt8, sa_family_t, UInt16, UInt16, UnsafeRawPointer) -> vmnet_return_t](vmnet_network_configuration_add_port_forwarding_rule(_:_:_:_:_:_:).md)
  Configures a new port forwarding rule for a vmnet network.
- [func vmnet_network_configuration_disable_router_advertisement(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_router_advertisement(_:).md)
  Disables router advertisement on a network.
- [func vmnet_network_configuration_disable_nat66(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_nat66(_:).md)
  Disables NAT66 on a network.
- [func vmnet_network_configuration_disable_nat44(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_nat44(_:).md)
  Disables NAT44 on a network.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_disable_dns_proxy(_:))*