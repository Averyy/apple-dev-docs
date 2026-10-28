# MPThrowException

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Throws an exception to a specified task.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPThrowException(MPTaskID task, MPExceptionKind kind);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If the task is already suspended or if the task is not defined to take thrown exceptions, the function returns `kMPInsufficientResourcesErr`.

## Discussion

The exception is treated in the same manner as any other exception taken by a task. However, since it is asynchronous, it may not be presented immediately.

By convention, you should set the exception kind to `kMPTaskStoppedErr` if you want to suspend a task. In general, you should do so only if you are debugging and wish to examine the state of the task. Otherwise you should block the task using one of the traditional notification mechanisms (such as a message queue). 

An exception can be thrown at any time, whether that task is running, eligible to be run (that is, ready), or blocked. The task is suspended and an exception message may be generated the next time the task is about to run. Note that this may never occur— for example, if the task is deadlocked or the resource it is waiting on is never released. If the task is currently blocked when this function is executed, `kMPTaskBlockedErr` is returned. If the task was suspended immediately at the conclusion of this function call the return value is `kMPTaskStoppedErr`.

In macOS, this function is available but is not implemented.

## Parameters

- `task`: The task to which the exception should be thrown. 
- `kind`: The type of exception to give to the task. 

## See Also

### Exception Handling Functions
- [MPDisposeTaskException](./api-1585607-mpdisposetaskexception.md)
  Removes a task exception.
- [MPExtractTaskState](./api-1585718-mpextracttaskstate.md)
  Extracts state information from a suspended task.
- [MPSetExceptionHandler](./api-1585759-mpsetexceptionhandler.md)
  Sets an exception handler for a task. 
- [MPSetTaskState](./api-1585601-mpsettaskstate.md)
  Sets state information for a suspended task. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585743-mpthrowexception)*