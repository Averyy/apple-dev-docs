# Cancel

**Framework**: Kernel  
**Kind**: instm

Stops the queue from dequeueing any further tasks, and notifies the specified handler when all in-flight tasks finish.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
kern_return_t Cancel(IODispatchQueueCancelHandler handler);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see `Error Codes`. 

#### Discussion

This method asynchronously tells the dispatch queue to stop the execution of queued tasks, and returns immediately. If a task is already executing, that task runs to completion. After all tasks finish, the dispatch queue executes the block in the `handler` parameter.

## Parameters

- `handler`: The block to execute when the queue finishes all in-flight work. 

## See Also

- [IODispatchQueueCancelHandler](../driverkit/iodispatchqueuecancelhandler.md)
  A block to execute when a canceled dispatch queue stops executing tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue/3438188-cancel)*