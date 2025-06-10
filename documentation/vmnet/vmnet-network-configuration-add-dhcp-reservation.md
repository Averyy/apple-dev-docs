# vmnet_network_configuration_add_dhcp_reservation(_:_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
func vmnet_network_configuration_add_dhcp_reservation(_ network: vmnet_network_configuration_ref, _ client: UnsafePointer<ether_addr_t>, _ reservation: UnsafePointer<in_addr>) -> vmnet_return_t
```

#### Return Value

VMNET_SUCCESS on success, error otherwise.

#### Discussion

Configures a new dhcp reservation for a vmnet network.

Reserve a DHCP address for a client with certain MAC address. Note that modifying reservation is not allowed while a network is active.

## Parameters

- `network`: The network object to be modified.
- `client`: The mac address for which the DHCP address is reserved.
- `reservation`: The DHCP address to be reserved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_add_dhcp_reservation(_:_:_:))*