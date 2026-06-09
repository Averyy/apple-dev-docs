# vmnet_network_configuration_create(_:_:)

**Framework**: vmnet  
**Kind**: func

Creates a network configuration object with the specified operating mode.

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_configuration_create(_ mode: vmnet_mode_t, _ status: UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_configuration_ref?
```

#### Return Value

A vmnet network handle on success, otherwise `NULL`.

#### Discussion

All other parameters are optional and have the following default value:

- External interface: default interface per the routing table
- NAT44: enabled
- NAT66: enabled
- DHCP: enabled
- DNS proxy: enabled
- Router advertisement: enabled
- IPv4 subnet: A /24 suffix, under 192.168/16 (the private address space defined by RFC-1918).
- IPv6 prefix: random Unique Local Addresses (ULA) prefix
- Port forwarding rule: none
- DHCP reservation: none
- MTU: 1500

Use [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) to release the network configuration object.

## Parameters

- `mode`: Shared mode or host-only mode.
- `status`: Optional output parameter, returns status.

## See Also

- [func vmnet_network_create(vmnet_network_configuration_ref, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?](vmnet_network_create(_:_:).md)
  Creates a vmnet network based on the provided configuration.
- [func vmnet_network_create_with_serialization(xpc_object_t, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?](vmnet_network_create_with_serialization(_:_:).md)
  Creates a vmnet network from an XPC object you obtained from calling the vmnet networkcopy serialization API.
- [func vmnet_network_copy_serialization(vmnet_network_ref, UnsafeMutablePointer<vmnet_return_t>?) -> xpc_object_t?](vmnet_network_copy_serialization(_:_:).md)
  Serializes a vmnet network to an XPC object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_create(_:_:))*