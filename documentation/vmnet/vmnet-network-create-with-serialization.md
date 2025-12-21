# vmnet_network_create_with_serialization(_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_network_create_with_serialization(_ network: xpc_object_t, _ status: UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?
```

#### Return Value

Network object in `vmnet_network_ref`, NULL otherwise. `status` will contain the error code.

#### Discussion

Creates a vmnet_network from an xpc object obtained from `vmnet_network_copy_serialization`.

## Parameters

- `network`: The xpc object from which to create the network
- `status`: Optional output parameter, returns status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_create_with_serialization(_:_:))*