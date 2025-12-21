# vmnet_interface_start_with_network(_:_:_:_:)

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
func vmnet_interface_start_with_network(_ network: vmnet_network_ref, _ interface_desc: xpc_object_t, _ queue: dispatch_queue_t, _ start_block: @escaping vmnet_start_interface_completion_handler_t) -> interface_ref?
```

#### Return Value

Returns a non-NULL interface handle on success, NULL otherwise.

#### Discussion

Starts a new virtual interface instance on a network.

Attributes of the virtual interface are specified using the `interface_desc dictionary`. Namely,

- `vmnet_allocate_mac_address_key`,
- `vmnet_enable_tso_key`,
- `vmnet_enable_isolation_key`,
- `vmnet_enable_checksum_offload_key`. On success, this call retains the network object.

## Parameters

- `network`: The network that the interface will be added to.
- `interface_desc`: A dictionary describing parameters to use when creating the interface.
- `queue`: The queue on which to schedule the completion handler.
- `start_block`: The block to invoke when the start interface request completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_interface_start_with_network(_:_:_:_:))*