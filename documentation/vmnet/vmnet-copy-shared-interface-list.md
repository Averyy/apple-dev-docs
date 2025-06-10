# vmnet_copy_shared_interface_list()

**Framework**: vmnet  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
func vmnet_copy_shared_interface_list() -> xpc_object_t?
```

## See Also

- [func vmnet_interface_add_ip_port_forwarding_rule(interface_ref, UInt8, UInt16, UInt8, UnsafeRawPointer, UInt16, vmnet_interface_completion_handler_t?) -> vmnet_return_t](vmnet_interface_add_ip_port_forwarding_rule(_:_:_:_:_:_:_:).md)
- [func vmnet_interface_add_port_forwarding_rule(interface_ref, UInt8, UInt16, in_addr, UInt16, vmnet_interface_completion_handler_t?) -> vmnet_return_t](vmnet_interface_add_port_forwarding_rule(_:_:_:_:_:_:).md)
- [func vmnet_interface_get_ip_port_forwarding_rules(interface_ref, UInt8, vmnet_interface_get_ip_port_forwarding_rules_handler_t) -> vmnet_return_t](vmnet_interface_get_ip_port_forwarding_rules(_:_:_:).md)
- [func vmnet_interface_get_port_forwarding_rules(interface_ref, vmnet_interface_get_port_forwarding_rules_handler_t) -> vmnet_return_t](vmnet_interface_get_port_forwarding_rules(_:_:).md)
- [func vmnet_interface_remove_ip_port_forwarding_rule(interface_ref, UInt8, UInt16, UInt8, vmnet_interface_completion_handler_t?) -> vmnet_return_t](vmnet_interface_remove_ip_port_forwarding_rule(_:_:_:_:_:).md)
- [func vmnet_interface_remove_port_forwarding_rule(interface_ref, UInt8, UInt16, vmnet_interface_completion_handler_t?) -> vmnet_return_t](vmnet_interface_remove_port_forwarding_rule(_:_:_:_:).md)
- [func vmnet_ip_port_forwarding_rule_get_details(xpc_object_t, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt16>, UInt8, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt16>) -> vmnet_return_t](vmnet_ip_port_forwarding_rule_get_details(_:_:_:_:_:_:).md)
- [func vmnet_port_forwarding_rule_get_details(xpc_object_t, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<in_addr>, UnsafeMutablePointer<UInt16>) -> vmnet_return_t](vmnet_port_forwarding_rule_get_details(_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_copy_shared_interface_list())*