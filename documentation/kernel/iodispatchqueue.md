# IODispatchQueue

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.15+

## Declaration

```swift
class IODispatchQueue : OSObject, IODispatchQueueInterface
```

## Topics

### Instance Methods
- [- Cancel](iodispatchqueue/3438188-cancel.md)
  Stops the queue from dequeueing any further tasks, and notifies the specified handler when all in-flight tasks finish.
- [- Dispatch](iodispatchqueue/3223267-dispatch.md)
- [- DispatchAsync](iodispatchqueue/3438190-dispatchasync.md)
  Schedule a block for asynchronous execution on the current queue.
- [- DispatchAsync_f](iodispatchqueue/3438191-dispatchasync_f.md)
  Schedule a C-style function for asynchrous execution on the current queue.
- [- DispatchConcurrent](../driverkit/iodispatchqueue/dispatchconcurrent.md)
- [- DispatchConcurrent_f](../driverkit/iodispatchqueue/dispatchconcurrent_f.md)
- [- DispatchSync](iodispatchqueue/3438192-dispatchsync.md)
  Schedule a block for synchronous execution on the current queue.
- [- DispatchSync_f](iodispatchqueue/3438193-dispatchsync_f.md)
  Schedule a C-style function for synchronous execution on the current queue.
- [- GetName](iodispatchqueue/3438194-getname.md)
  Returns the name of the queue as a C string.
- [- OnQueue](iodispatchqueue/3438196-onqueue.md)
  Returns a Boolean value that indicates whether the current thread matches the dispatch queue's thread. 
- [- RunAction](../driverkit/iodispatchqueue/runaction.md)
- [- SetPort](iodispatchqueue/3223275-setport.md)
- [- SetPort_Impl](iodispatchqueue/3223276-setport_impl.md)
- [- Sleep](../driverkit/iodispatchqueue/sleep.md)
- [- SleepWithDeadline](../driverkit/iodispatchqueue/sleepwithdeadline.md)
- [- SleepWithTimeout](../driverkit/iodispatchqueue/sleepwithtimeout.md)
- [- Wakeup](../driverkit/iodispatchqueue/wakeup.md)
- [- WakeupWithOptions](../driverkit/iodispatchqueue/wakeupwithoptions.md)
- [- free](iodispatchqueue/3438197-free.md)
  Performs any final cleanup for the dispatch queue object.
- [- getMetaClass](iodispatchqueue/3223279-getmetaclass.md)
- [- init](iodispatchqueue/3438198-init.md)
  Initializes the dispatch queue object.
### Type Methods
- [+ Create](iodispatchqueue/3438189-create.md)
  Creates a new dispatch queue object.
- [+ Create_Call](iodispatchqueue/3223264-create_call.md)
- [+ Create_Impl](iodispatchqueue/3223265-create_impl.md)
- [+ Create_Invoke](iodispatchqueue/3223266-create_invoke.md)
- [+ Log](iodispatchqueue/3438195-log.md)
  Log the current execution context with respect to any queues the current thread holds.
- [+ SetPort_Invoke](iodispatchqueue/3223277-setport_invoke.md)

## Relationships

### Inherits From
- [IODispatchQueueInterface](iodispatchqueueinterface.md)
- [OSObject](osobject.md)

## See Also

- [IODispatchQueueInterface](iodispatchqueueinterface.md)
- [IODispatchSourceInterface](iodispatchsourceinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue)*