# semaphore_wait_deadline

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.6+

## Declaration

```c
kern_return_t semaphore_wait_deadline(semaphore_t semaphore, uint64_t deadline);
```

## See Also

### Semaphore
- [semaphore_create](./api-1538205-semaphore_create.md)
- [semaphore_destroy](./api-1537823-semaphore_destroy.md)
- [semaphore_signal](./api-1585827-semaphore_signal.md)
- [semaphore_signal_all](./api-1585830-semaphore_signal_all.md)
- [semaphore_wait](./api-1585828-semaphore_wait.md)
- [semaphore_wait_noblock](./api-1585826-semaphore_wait_noblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585829-semaphore_wait_deadline)*