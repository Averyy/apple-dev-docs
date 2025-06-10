# vmnet_network_copy_serialization(_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+ (Beta)

## Declaration

```swift
func vmnet_network_copy_serialization(_ network: vmnet_network_ref, _ status: UnsafeMutablePointer<vmnet_return_t>?) -> xpc_object_t?
```

#### Return Value

Serialized copy of network in `xpc_object_t`, NULL otherwise. Optionally, `status` will contain the error code.

#### Discussion

Copy serializes a vmnet network to an xpc object. Use `vmnet_network_create_with_serialization` to create a new network object from such xpc object.

## Parameters

- `network`: The network object to be copy serialized.
- `status`: Optional output parameter, returns status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_network_copy_serialization(_:_:))*