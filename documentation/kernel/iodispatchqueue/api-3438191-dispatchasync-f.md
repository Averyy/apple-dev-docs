# DispatchAsync_f

**Framework**: Kernel  
**Kind**: instm

Schedule a C-style function for asynchrous execution on the current queue.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
void DispatchAsync_f(void *context, IODispatchFunction function);
```

#### Discussion

This method schedules the function for execution on the queue and returns immediately, without waiting for execution of the function to begin. The system retains the queue until the function completes.

## Parameters

- `context`: A pointer to contextual data that you want to pass to the function.
- `function`: The function to execute on the queue.

## See Also

- [IODispatchBlock](../driverkit/iodispatchblock.md)
  A block to execute on a dispatch queue.
- [IODispatchFunction](../driverkit/iodispatchfunction.md)
  A C-style function to execute on a dispatch queue.
- [- DispatchAsync](iodispatchqueue/3438190-dispatchasync.md)
  Schedule a block for asynchronous execution on the current queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue/3438191-dispatchasync_f)*