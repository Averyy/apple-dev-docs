# MPSetExceptionHandler

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets an exception handler for a task. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPSetExceptionHandler(MPTaskID task, MPQueueID exceptionQ);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

When an exception handler is set and an exception occurs, the task is suspended and a message is sent to the message queue specified by `exceptionQ`. The message contains the following information:

-  The first pointer-sized value contains the ID of the task in which the exception occurred. 
-  The second pointer-sized value contains the type of exception that occurred. See the header file `MachineExceptions.h` for a listing of exception types.  
-  The last pointer-sized value is set to `NULL` (reserved for future use).

## Parameters

- `task`: The task to associate with the exception handler. 
- `exceptionQ`: The message queue to which an exception message will be sent. 

## See Also

### Exception Handling Functions
- [MPDisposeTaskException](./api-1585607-mpdisposetaskexception.md)
  Removes a task exception.
- [MPExtractTaskState](./api-1585718-mpextracttaskstate.md)
  Extracts state information from a suspended task.
- [MPSetTaskState](./api-1585601-mpsettaskstate.md)
  Sets state information for a suspended task. 
- [MPThrowException](./api-1585743-mpthrowexception.md)
  Throws an exception to a specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585759-mpsetexceptionhandler)*