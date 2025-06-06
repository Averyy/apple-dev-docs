# semaphore_create

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t semaphore_create(task_t task, semaphore_t *semaphore, int policy, int value);
```

## See Also

- [semaphore_destroy](1537823-semaphore_destroy.md)
- [semaphore_signal](1585827-semaphore_signal.md)
- [semaphore_signal_all](1585830-semaphore_signal_all.md)
- [semaphore_wait](1585828-semaphore_wait.md)
- [semaphore_wait_deadline](1585829-semaphore_wait_deadline.md)
- [semaphore_wait_noblock](1585826-semaphore_wait_noblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1538205-semaphore_create)*