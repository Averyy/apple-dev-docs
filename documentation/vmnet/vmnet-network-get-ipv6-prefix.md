# vmnet_network_get_ipv6_prefix(_:_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
func vmnet_network_get_ipv6_prefix(_ network: vmnet_network_ref, _ prefix: UnsafeMutablePointer<in6_addr>, _ prefix_len: UnsafeMutablePointer<UInt8>)
```

#### Discussion

Queries the IPv6 prefix of a network.

Gives the reserved IPv6 prefix when it was kept at default.

## Parameters

- `network`: The network object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_get_ipv6_prefix(_:_:_:))*