# vmnet_stop_interface(_:_:_:)

**Framework**: vmnet  
**Kind**: func

Stops I/O on the virtual interface.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
func vmnet_stop_interface(_ interface: interface_ref, _ queue: dispatch_queue_t, _ handler: @escaping vmnet_interface_completion_handler_t) -> vmnet_return_t
```

#### Return Value

`VMNET_SUCCESS` if the framework scheduled the completion handler, an error code otherwise.

#### Discussion

Once an app calls this function, subsequent calls to read or write packets on this interface fail. If the app created the  interface through [`vmnet_interface_start_with_network(_:_:_:_:)`](vmnet_interface_start_with_network(_:_:_:_:).md), this call releases the associated network object.

## Parameters

- `interface`: The interface to halt I/O on.
- `queue`: The queue to schedule the stop handler on.
- `handler`: The block that is invoked when the stop interface request completes.

## See Also

- [func vmnet_start_interface(xpc_object_t, dispatch_queue_t, vmnet_start_interface_completion_handler_t) -> interface_ref?](vmnet_start_interface(_:_:_:).md)
  Starts a new virtual interface instance.
- [func vmnet_interface_start_with_network(vmnet_network_ref, xpc_object_t, dispatch_queue_t, vmnet_start_interface_completion_handler_t) -> interface_ref?](vmnet_interface_start_with_network(_:_:_:_:).md)
  Starts a new virtual interface instance on a network.
- [func vmnet_interface_set_event_callback(interface_ref, interface_event_t, dispatch_queue_t?, vmnet_interface_event_callback_t?) -> vmnet_return_t](vmnet_interface_set_event_callback(_:_:_:_:).md)
  Schedules a callback to be executed when events for the specified interface are received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_stop_interface(_:_:_:))*