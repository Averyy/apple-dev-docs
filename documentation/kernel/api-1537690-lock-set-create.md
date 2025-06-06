# lock_set_create

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t lock_set_create(task_t task, lock_set_t *new_lock_set, int n_ulocks, int policy);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1537690-lock_set_create)*