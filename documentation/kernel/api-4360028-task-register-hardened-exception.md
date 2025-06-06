# task_register_hardened_exception_handler

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 15.0+

## Declaration

```swift
kern_return_t task_register_hardened_exception_handler(task_t task, uint32_t signed_pc_key, exception_mask_t exceptions_allowed, exception_behavior_t behaviors_allowed, thread_state_flavor_t flavors_allowed, mach_port_t new_exception_port);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4360028-task_register_hardened_exception)*