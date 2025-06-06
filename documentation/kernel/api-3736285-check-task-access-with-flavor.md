# check_task_access_with_flavor

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 11.3+

## Declaration

```swift
kern_return_t check_task_access_with_flavor(mach_port_t task_access_port, int32_t calling_pid, uint32_t calling_gid, int32_t target_pid, mach_task_flavor_t flavor);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3736285-check_task_access_with_flavor)*