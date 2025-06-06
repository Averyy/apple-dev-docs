# thread_convert_thread_state

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 11.0+

## Declaration

```swift
kern_return_t thread_convert_thread_state(thread_act_t thread, int direction, thread_state_flavor_t flavor, thread_state_t in_state, mach_msg_type_number_t in_stateCnt, thread_state_t out_state, mach_msg_type_number_t *out_stateCnt);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3553733-thread_convert_thread_state)*