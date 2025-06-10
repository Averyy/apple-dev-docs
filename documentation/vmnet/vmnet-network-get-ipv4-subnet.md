# vmnet_network_get_ipv4_subnet(_:_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
func vmnet_network_get_ipv4_subnet(_ network: vmnet_network_ref, _ subnet: UnsafeMutablePointer<in_addr>, _ mask: UnsafeMutablePointer<in_addr>)
```

#### Discussion

Queries the IPv4 subnet of a network.

Gives the reserved IPv4 subnet when it was kept at default.

## Parameters

- `network`: The network object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_get_ipv4_subnet(_:_:_:))*