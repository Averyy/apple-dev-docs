# vmnet_network_create(_:_:)

**Framework**: vmnet  
**Kind**: func

Creates a vmnet network based on the provided configuration.

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_create(_ configuration: vmnet_network_configuration_ref, _ status: UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?
```

#### Return Value

Vmnet network handle on success, otherwise `NULL`.

#### Discussion

This API attempts to reserve the configuration such that subsequent interface start calls is guaranteed to not fail due to resource contention. The lifetime of such reservation is the same as that of [`vmnet_network_ref`](vmnet_network_ref.md). Use [`CFRelease`](https://developer.apple.com/documentation/corefoundation/cfrelease) to release the network object.

## Parameters

- `configuration`: The vmnet network configuration.

## See Also

- [func vmnet_network_configuration_create(vmnet_mode_t, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_configuration_ref?](vmnet_network_configuration_create(_:_:).md)
  Creates a network configuration object with the specified operating mode.
- [func vmnet_network_create_with_serialization(xpc_object_t, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?](vmnet_network_create_with_serialization(_:_:).md)
  Creates a vmnet network from an XPC object you obtained from calling the vmnet networkcopy serialization API.
- [func vmnet_network_copy_serialization(vmnet_network_ref, UnsafeMutablePointer<vmnet_return_t>?) -> xpc_object_t?](vmnet_network_copy_serialization(_:_:).md)
  Serializes a vmnet network to an XPC object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_create(_:_:))*