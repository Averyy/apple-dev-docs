# MPSetTaskState

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets state information for a suspended task. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPSetTaskState(MPTaskID task, MPTaskStateKind kind, void *info);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If you specify `kMPTaskState32BitMemoryException` for the state information, this function returns `kMPInsufficientResourcesErr`, since the exception state information is read-only. Attempting to set state information for a running task will also return `kMPInsufficientResourcesErr`.

## Discussion

You can use this function to set register contents or exception information for a particular task. However, some state information, such as the exception information (as specified by `kMPTaskState32BitMemoryException`) as well as the `MSR`, `ExceptKind`, `DSISR`, and `DAR` machine registers (specified under `kMPTaskStateMachine`) are read-only. Attempting to set the read-only machine registers will do nothing, while attempting to set the exception information will return an error. 

Also see the function  [`MPExtractTaskState`](./api-1585718-mpextracttaskstate.md). 

## Parameters

- `task`: The task whose state information you want to set. 
- `kind`: The kind of state information you want to set. See [Task State Constants](./api-1585773-task_state_constants.md) for a listing of possible values. Note that some state information is read-only and cannot be changed using this function. 
- `info`: A pointer to a data structure holding the state information you want to set. The format of the data structure varies depending on the state information you want to set. See the header file `MachineExceptions.h` for the formats of the various state information structures. 

## See Also

### Exception Handling Functions
- [MPDisposeTaskException](./api-1585607-mpdisposetaskexception.md)
  Removes a task exception.
- [MPExtractTaskState](./api-1585718-mpextracttaskstate.md)
  Extracts state information from a suspended task.
- [MPSetExceptionHandler](./api-1585759-mpsetexceptionhandler.md)
  Sets an exception handler for a task. 
- [MPThrowException](./api-1585743-mpthrowexception.md)
  Throws an exception to a specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585601-mpsettaskstate)*