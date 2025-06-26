# vmnet_network_configuration_add_port_forwarding_rule(_:_:_:_:_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
func vmnet_network_configuration_add_port_forwarding_rule(_ config: vmnet_network_configuration_ref, _ protocol: UInt8, _ address_family: sa_family_t, _ internal_port: UInt16, _ external_port: UInt16, _ internal_address: UnsafeRawPointer) -> vmnet_return_t
```

#### Return Value

VMNET_SUCCESS on success, error otherwise.

#### Discussion

Configures a new port forwarding rule for a vmnet network. These rules will not be able to be removed or queried until network has been started. To do that, use `vmnet_interface_remove_ip_forwarding_rule` or `vmnet_interface_get_ip_port_forwarding_rules` APIs, respectively.

## Parameters

- `config`: The network configuration object to be modified.
- `protocol`: The protocol to apply the port forwarding rule to.   Must be either IPPROTO_TCP or IPPROTO_UDP (see <netinet/in.h>).
- `address_family`: The address family (AF_INET or AF_INET6) of ‘internal_address’. If   AF_INET, ‘internal address’ must point to a ‘struct in_addr’. If   AF_INET6, ‘internal_address’ must point to a “struct in6_addr’.
- `internal_port`: The TCP or UDP port that the forwarded traffic should be redirected to.   Must be in host byte order.
- `external_port`: The TCP or UDP port on the outside network that should be redirected from.   Must be in host byte order.
- `internal_address`: Pointer to IPv4 or IPv6 address of the machine on the internal network that   should receive the forwarded traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_add_port_forwarding_rule(_:_:_:_:_:_:))*