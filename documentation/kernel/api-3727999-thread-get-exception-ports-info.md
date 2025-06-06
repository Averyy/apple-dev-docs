# thread_get_exception_ports_info

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 11.3+

## Declaration

```swift
kern_return_t thread_get_exception_ports_info(mach_port_t port, exception_mask_t exception_mask, exception_mask_array_t masks, mach_msg_type_number_t *masksCnt, exception_handler_info_array_t old_handlers_info, exception_behavior_array_t old_behaviors, exception_flavor_array_t old_flavors);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3727999-thread_get_exception_ports_info)*