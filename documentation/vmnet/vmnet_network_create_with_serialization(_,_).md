# vmnet_network_create_with_serialization(_:_:)

**Framework**: vmnet  
**Kind**: func  
**Role**: Function

Creates a vmnet network from an XPC object you obtained from calling the vmnet networkcopy serialization API.

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_create_with_serialization(_ network: xpc_object_t, _ status: UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?
```

```c
vmnet_network_refvmnet_network_create_with_serialization(xpc_object_t network, vmnet_return_t *status);
```

#### Return Value

Network object in [`vmnet_network_ref`](./vmnet_network_ref.md), `NULL` otherwise. The `status` contains the error code.

## Parameters

- `network`: The xpc object from which to create the network
- `status`: Optional output parameter, returns status.

## See Also

### Creating a network configuration
- [func vmnet_network_create(vmnet_network_configuration_ref, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?](./vmnet_network_create%28_,_%29.md)
  Creates a vmnet network based on the provided configuration.
- [func vmnet_network_configuration_create(vmnet_mode_t, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_configuration_ref?](./vmnet_network_configuration_create%28_,_%29.md)
  Creates a network configuration object with the specified operating mode.
- [func vmnet_network_copy_serialization(vmnet_network_ref, UnsafeMutablePointer<vmnet_return_t>?) -> xpc_object_t?](./vmnet_network_copy_serialization%28_,_%29.md)
  Serializes a vmnet network to an XPC object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_create_with_serialization(_:_:))*