# vmnet_start_interface(_:_:_:)

**Framework**: vmnet  
**Kind**: func  
**Role**: Function

Starts a new virtual interface instance.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
func vmnet_start_interface(_ interface_desc: xpc_object_t, _ queue: dispatch_queue_t, _ handler: @escaping vmnet_start_interface_completion_handler_t) -> interface_ref?
```

```c
interface_refvmnet_start_interface(xpc_object_t interface_desc, dispatch_queue_t queue, vmnet_start_interface_completion_handler_t handler);
```

## Return Value

A non-`NULL` interface handle on success, `NULL` otherwise.

## Discussion

Attributes of the virtual interface are specified using the interface_desc dictionary.

## Parameters

- `interface_desc`: A dictionary describing parameters to use when creating the interface.
- `queue`: The queue on which to schedule the completion handler.
- `handler`: The block to invoke when the start interface request completes.

## See Also

### Starting and stopping interfaces
- [func vmnet_interface_start_with_network(vmnet_network_ref, xpc_object_t, dispatch_queue_t, vmnet_start_interface_completion_handler_t) -> interface_ref?](./vmnet_interface_start_with_network%28_,_,_,_%29.md)
  Starts a new virtual interface instance on a network.
- [func vmnet_interface_set_event_callback(interface_ref, interface_event_t, dispatch_queue_t?, vmnet_interface_event_callback_t?) -> vmnet_return_t](./vmnet_interface_set_event_callback%28_,_,_,_%29.md)
  Schedules a callback to be executed when events for the specified interface are received.
- [func vmnet_stop_interface(interface_ref, dispatch_queue_t, vmnet_interface_completion_handler_t) -> vmnet_return_t](./vmnet_stop_interface%28_,_,_%29.md)
  Stops I/O on the virtual interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_start_interface(_:_:_:))*