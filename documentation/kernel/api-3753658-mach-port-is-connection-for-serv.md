# mach_port_is_connection_for_service

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
kern_return_t mach_port_is_connection_for_service(ipc_space_t task, mach_port_name_t connection_port, mach_port_name_t service_port, uint64_t *filter_policy_id);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3753658-mach_port_is_connection_for_serv)*