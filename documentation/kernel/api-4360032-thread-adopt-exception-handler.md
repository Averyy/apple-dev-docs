# thread_adopt_exception_handler

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 15.0+

## Declaration

```swift
kern_return_t thread_adopt_exception_handler(thread_t thread, mach_port_t exc_port, exception_mask_t exc_mask, exception_behavior_t behavior_mask, thread_state_flavor_t flavor_mask);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4360032-thread_adopt_exception_handler)*