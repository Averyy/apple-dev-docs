# vmnet_network_create(_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_create(_ configuration: vmnet_network_configuration_ref, _ status: UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?
```

#### Return Value

Vmnet network handle on success, otherwise NULL.

#### Discussion

Creates a vmnet network based on the configuration.

This API attempts to reserve the configuration such that subsequent interface start calls is guaranteed to not fail due to resource contention. The lifetime of such reservation is the same as that of `vmnet_network_ref`. Use `CFRelease()` to release the network object.

## Parameters

- `configuration`: The vmnet network configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_create(_:_:))*