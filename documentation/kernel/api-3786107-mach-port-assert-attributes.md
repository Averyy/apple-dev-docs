# mach_port_assert_attributes

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
kern_return_t mach_port_assert_attributes(ipc_space_t task, mach_port_name_t name, mach_port_flavor_t flavor, mach_port_info_t info, mach_msg_type_number_t infoCnt);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3786107-mach_port_assert_attributes)*