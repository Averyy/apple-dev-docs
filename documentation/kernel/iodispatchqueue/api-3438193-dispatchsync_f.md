# DispatchSync_f

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Schedule a C-style function for synchronous execution on the current queue.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
void DispatchSync_f(void *context, IODispatchFunction function);
```

## Discussion

This method schedules the function for execution on the queue and waits for it to complete before returning. The system retains the queue until the function completes.

## Parameters

- `context`: A pointer to contextual data that you want to pass to the function.
- `function`: The function to execute on the queue.

## See Also

### Executing a Task Synchronously
- [- DispatchSync](./api-3438192-dispatchsync.md)
  Schedule a block for synchronous execution on the current queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue/3438193-dispatchsync_f)*