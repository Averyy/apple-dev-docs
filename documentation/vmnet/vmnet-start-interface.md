# vmnet_start_interface(_:_:_:)

**Framework**: Vmnet  
**Kind**: func

Starts host or shared mode on an interface with a specified configuration.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
func vmnet_start_interface(_ interface_desc: xpc_object_t, _ queue: dispatch_queue_t, _ handler: @escaping vmnet_start_interface_completion_handler_t) -> interface_ref?
```

#### Return Value

Returns an interface reference, or `NULL` if an error occurred.

## Parameters

- `interface_desc`: An XPC dictionary describing parameters of the interface.   Supported keys are described in  .
- `queue`: The queue on which the handler is scheduled.
- `handler`: A block to be executed after interface is started.

## See Also

- [func vmnet_interface_set_event_callback(interface_ref, interface_event_t, dispatch_queue_t?, vmnet_interface_event_callback_t?) -> vmnet_return_t](vmnet_interface_set_event_callback(_:_:_:_:).md)
  Schedules a callback to be executed when events for the specified interface are received.
- [func vmnet_stop_interface(interface_ref, dispatch_queue_t, vmnet_interface_completion_handler_t) -> vmnet_return_t](vmnet_stop_interface(_:_:_:).md)
  Stops the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_start_interface(_:_:_:))*