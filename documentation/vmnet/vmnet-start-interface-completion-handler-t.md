# vmnet_start_interface_completion_handler_t

**Framework**: vmnet  
**Kind**: typealias

The type of the block provided in the call to vmnet_start_interface

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
typealias vmnet_start_interface_completion_handler_t = (vmnet_return_t, xpc_object_t?) -> Void
```

#### Discussion

- Parfameters: - status: If status is `VMNET_SUCCESS`, the framework created the interface successfully. Otherwise, the interface failed to be created.
- interface_param: A dictionary containing interface parameters that describe the interface.

## See Also

- [typealias vmnet_interface_completion_handler_t](vmnet_interface_completion_handler_t.md)
- [typealias vmnet_interface_event_callback_t](vmnet_interface_event_callback_t.md)
- [typealias vmnet_interface_get_ip_port_forwarding_rules_handler_t](vmnet_interface_get_ip_port_forwarding_rules_handler_t.md)
- [typealias vmnet_interface_get_port_forwarding_rules_handler_t](vmnet_interface_get_port_forwarding_rules_handler_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_start_interface_completion_handler_t)*