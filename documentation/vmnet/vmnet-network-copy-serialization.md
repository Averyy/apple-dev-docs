# vmnet_network_copy_serialization(_:_:)

**Framework**: vmnet  
**Kind**: func

Serializes a vmnet network to an XPC object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_copy_serialization(_ network: vmnet_network_ref, _ status: UnsafeMutablePointer<vmnet_return_t>?) -> xpc_object_t?
```

#### Return Value

Serialized copy of network in `xpc_object_t`, `NULL` otherwise. Optionally, `status` will contain the error code.

#### Discussion

Use `vmnet_network_create_with_serialization` to create a new network object from such an XPC object.

## Parameters

- `network`: The network object to be copy serialized.
- `status`: Optional output parameter, returns status.

## See Also

- [func vmnet_network_create(vmnet_network_configuration_ref, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?](vmnet_network_create(_:_:).md)
  Creates a vmnet network based on the provided configuration.
- [func vmnet_network_configuration_create(vmnet_mode_t, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_configuration_ref?](vmnet_network_configuration_create(_:_:).md)
  Creates a network configuration object with the specified operating mode.
- [func vmnet_network_create_with_serialization(xpc_object_t, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?](vmnet_network_create_with_serialization(_:_:).md)
  Creates a vmnet network from an XPC object you obtained from calling the vmnet networkcopy serialization API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_copy_serialization(_:_:))*