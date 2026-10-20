# vmnet_interface_remove_port_forwarding_rule(_:_:_:_:)

**Framework**: vmnet  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+ - Deprecated in 12.0

> **Deprecated**: replaced by vmnet_interface_remove_ip_port_forwarding_rule

## Declaration

```swift
func vmnet_interface_remove_port_forwarding_rule(_ interface: interface_ref, _ protocol: UInt8, _ external_port: UInt16, _ handler: vmnet_interface_completion_handler_t?) -> vmnet_return_t
```

```c
vmnet_return_t vmnet_interface_remove_port_forwarding_rule(interface_ref interface, uint8_t protocol, uint16_t external_port, vmnet_interface_completion_handler_t handler);
```

## See Also

### Functions
- [func vmnet_copy_shared_interface_list() -> xpc_object_t?](./vmnet_copy_shared_interface_list%28%29.md)
- [func vmnet_interface_add_ip_port_forwarding_rule(interface_ref, UInt8, UInt16, UInt8, UnsafeRawPointer, UInt16, vmnet_interface_completion_handler_t?) -> vmnet_return_t](./vmnet_interface_add_ip_port_forwarding_rule%28_,_,_,_,_,_,_%29.md)
- [func vmnet_interface_add_port_forwarding_rule(interface_ref, UInt8, UInt16, in_addr, UInt16, vmnet_interface_completion_handler_t?) -> vmnet_return_t](./vmnet_interface_add_port_forwarding_rule%28_,_,_,_,_,_%29.md)
- [func vmnet_interface_get_ip_port_forwarding_rules(interface_ref, UInt8, vmnet_interface_get_ip_port_forwarding_rules_handler_t) -> vmnet_return_t](./vmnet_interface_get_ip_port_forwarding_rules%28_,_,_%29.md)
- [func vmnet_interface_get_port_forwarding_rules(interface_ref, vmnet_interface_get_port_forwarding_rules_handler_t) -> vmnet_return_t](./vmnet_interface_get_port_forwarding_rules%28_,_%29.md)
- [func vmnet_interface_remove_ip_port_forwarding_rule(interface_ref, UInt8, UInt16, UInt8, vmnet_interface_completion_handler_t?) -> vmnet_return_t](./vmnet_interface_remove_ip_port_forwarding_rule%28_,_,_,_,_%29.md)
- [func vmnet_ip_port_forwarding_rule_get_details(xpc_object_t, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt16>, UInt8, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt16>) -> vmnet_return_t](./vmnet_ip_port_forwarding_rule_get_details%28_,_,_,_,_,_%29.md)
- [func vmnet_port_forwarding_rule_get_details(xpc_object_t, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<in_addr>, UnsafeMutablePointer<UInt16>) -> vmnet_return_t](./vmnet_port_forwarding_rule_get_details%28_,_,_,_,_%29.md)
  Extracts port forwarding rule details from the rule XPC dictionary object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_interface_remove_port_forwarding_rule(_:_:_:_:))*