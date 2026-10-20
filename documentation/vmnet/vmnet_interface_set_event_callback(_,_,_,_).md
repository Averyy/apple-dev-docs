# vmnet_interface_set_event_callback(_:_:_:_:)

**Framework**: vmnet  
**Kind**: func  
**Role**: Function

Schedules a callback to be executed when events for the specified interface are received.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
func vmnet_interface_set_event_callback(_ interface: interface_ref, _ event_mask: interface_event_t, _ queue: dispatch_queue_t?, _ callback: vmnet_interface_event_callback_t?) -> vmnet_return_t
```

```c
vmnet_return_t vmnet_interface_set_event_callback(interface_ref interface, interface_event_t event_mask, dispatch_queue_t queue, vmnet_interface_event_callback_t callback);
```

#### Return Value

Returns `vmnet` on success, or an error code on failure. See `vmnet` for possible values.

#### Discussion

Once the block is set, the callback can be unset by calling the function again, specifying a `NULL` queue and a `NULL` handler.

## Parameters

- `interface`: The interface reference.
- `queue`: The queue on which the handler is scheduled.

## See Also

### Starting and stopping interfaces
- [func vmnet_start_interface(xpc_object_t, dispatch_queue_t, vmnet_start_interface_completion_handler_t) -> interface_ref?](./vmnet_start_interface%28_,_,_%29.md)
  Starts a new virtual interface instance.
- [func vmnet_interface_start_with_network(vmnet_network_ref, xpc_object_t, dispatch_queue_t, vmnet_start_interface_completion_handler_t) -> interface_ref?](./vmnet_interface_start_with_network%28_,_,_,_%29.md)
  Starts a new virtual interface instance on a network.
- [func vmnet_stop_interface(interface_ref, dispatch_queue_t, vmnet_interface_completion_handler_t) -> vmnet_return_t](./vmnet_stop_interface%28_,_,_%29.md)
  Stops I/O on the virtual interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_interface_set_event_callback(_:_:_:_:))*