# vmnet_network_configuration_set_mtu(_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
func vmnet_network_configuration_set_mtu(_ network: vmnet_network_configuration_ref, _ mtu: UInt32) -> vmnet_return_t
```

#### Return Value

VMNET_SUCCESS on success, error otherwise.

#### Discussion

Configures the maximum transmission unit (MTU) for a vmnet network.

## Parameters

- `network`: The network object to be modified.
- `mtu`: The MTU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_set_mtu(_:_:))*