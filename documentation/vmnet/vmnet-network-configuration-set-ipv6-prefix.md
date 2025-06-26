# vmnet_network_configuration_set_ipv6_prefix(_:_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
func vmnet_network_configuration_set_ipv6_prefix(_ config: vmnet_network_configuration_ref, _ prefix: UnsafePointer<in6_addr>, _ len: UInt8) -> vmnet_return_t
```

#### Return Value

VMNET_SUCCESS on success, error otherwise.

#### Discussion

Configures the IPv6 prefix for a vmnet network object.

## Parameters

- `config`: The network configuration object to be modified.
- `prefix`: The IPv6 prefix.
- `len`: The IPv6 prefix length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_set_ipv6_prefix(_:_:_:))*