# vmnet_network_configuration_create(_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
func vmnet_network_configuration_create(_ mode: vmnet_mode_t, _ status: UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_configuration_ref?
```

#### Return Value

Vmnet network handle on success, otherwise NULL.

#### Discussion

Creates a network configuration object with the specified operating mode.

All other parameters are optional and have the following default value:

- External interface: default interface per the routing table
- NAT44: enabled
- NAT66: enabled
- DHCP: enabled
- DNS proxy: enabled
- Router advertisement: enabled
- IPv4 subnet: a /24 under 192.168/16
- IPv6 prefix: random ULA prefix
- Port forwarding rule: none
- DHCP reservation: none
- MTU: 1500 Use `CFRelease()` to release the network configuration object.

## Parameters

- `mode`: Shared mode or host-only mode.
- `status`: Optional output parameter, returns status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_create(_:_:))*