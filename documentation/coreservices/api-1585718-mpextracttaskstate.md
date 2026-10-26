# MPExtractTaskState

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Extracts state information from a suspended task.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPExtractTaskState(MPTaskID task, MPTaskStateKind kind, void *info);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If you attempt to extract state information for a running task, this function returns `kMPInsufficientResourcesErr`.

#### Discussion

You can use this function to obtain register contents or exception information about a particular task. 

Also see the function  [`MPSetTaskState`](./api-1585601-mpsettaskstate.md). 

## Parameters

- `task`: The task whose state information you want to obtain. 
- `kind`: The kind of state information you want to obtain. See [Task State Constants](./api-1585773-task_state_constants.md) for a listing of possible values. 
- `info`: A pointer to a data structure to hold the state information. On return, the data structure holds the desired state information. The format of the data structure varies depending on the state information you want to retrieve. See the header file `MachineExceptions.h` for the formats of the various state information structures. 

## See Also

### Exception Handling Functions
- [MPDisposeTaskException](./api-1585607-mpdisposetaskexception.md)
  Removes a task exception.
- [MPSetExceptionHandler](./api-1585759-mpsetexceptionhandler.md)
  Sets an exception handler for a task. 
- [MPSetTaskState](./api-1585601-mpsettaskstate.md)
  Sets state information for a suspended task. 
- [MPThrowException](./api-1585743-mpthrowexception.md)
  Throws an exception to a specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585718-mpextracttaskstate)*