# vmnet_interface_get_ip_port_forwarding_rules_handler_t

**Framework**: vmnet  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
typealias vmnet_interface_get_ip_port_forwarding_rules_handler_t = (xpc_object_t?) -> Void
```

```c
typedef void (^)(NSObject<OS_xpc_object> *) vmnet_interface_get_ip_port_forwarding_rules_handler_t;
```

## See Also

### Data types
- [typealias vmnet_interface_completion_handler_t](./vmnet_interface_completion_handler_t.md)
- [typealias vmnet_interface_event_callback_t](./vmnet_interface_event_callback_t.md)
- [typealias vmnet_interface_get_port_forwarding_rules_handler_t](./vmnet_interface_get_port_forwarding_rules_handler_t.md)
- [typealias vmnet_start_interface_completion_handler_t](./vmnet_start_interface_completion_handler_t.md)
  The type of the block provided in the call to vmnet_start_interface


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_interface_get_ip_port_forwarding_rules_handler_t)*