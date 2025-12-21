# vmnet_network_configuration_set_ipv4_subnet(_:_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_configuration_set_ipv4_subnet(_ config: vmnet_network_configuration_ref, _ subnet_addr: UnsafePointer<in_addr>, _ subnet_mask: UnsafePointer<in_addr>) -> vmnet_return_t
```

#### Return Value

VMNET_SUCCESS on success, error otherwise.

#### Discussion

Configures the IPv4 addresses for a vmnet network. Note that the first, second, and last addresses of the range are reserved. The second address is reserved for the host, the first and last are not assignable to any node.

## Parameters

- `config`: The network configuration object to be modified.
- `subnet_addr`: The subnet address.
- `subnet_mask`: The subnet mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_set_ipv4_subnet(_:_:_:))*