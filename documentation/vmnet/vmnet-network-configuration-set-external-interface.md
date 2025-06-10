# vmnet_network_configuration_set_external_interface(_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
func vmnet_network_configuration_set_external_interface(_ network: vmnet_network_configuration_ref, _ interface_name: UnsafePointer<CChar>) -> vmnet_return_t
```

#### Return Value

VMNET_SUCCESS on success, error otherwise.

#### Discussion

Configures the external interface of a vmnet network.

This is only applicable to networks of `VMNET_SHARED_MODE`.

## Parameters

- `network`: The network object to be modified.
- `interface_name`: The name of the external interface


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_set_external_interface(_:_:))*