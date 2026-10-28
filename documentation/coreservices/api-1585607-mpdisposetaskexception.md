# MPDisposeTaskException

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Removes a task exception.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDisposeTaskException(MPTaskID task, OptionBits action);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If the specified action is invalid or unsupported, or if the specified task is not suspended, this function returns `kMPInsufficientResourcesErr`.

## Discussion

This function removes the task exception and allows the task to resume operation. If desired, you can enable single-stepping or branch-stepping, or propagate the exception instead.  

## Parameters

- `task`: The task whose exception you want to remove. 
- `action`: Any actions to perform on the task. For example, you can enable single-stepping when the task resumes, or you can pass the exception on to another handler. See [Task Exception Disposal Constants](./api-1585628-task_exception_disposal_constant.md) for a listing of possible values. 

## See Also

### Exception Handling Functions
- [MPExtractTaskState](./api-1585718-mpextracttaskstate.md)
  Extracts state information from a suspended task.
- [MPSetExceptionHandler](./api-1585759-mpsetexceptionhandler.md)
  Sets an exception handler for a task. 
- [MPSetTaskState](./api-1585601-mpsettaskstate.md)
  Sets state information for a suspended task. 
- [MPThrowException](./api-1585743-mpthrowexception.md)
  Throws an exception to a specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585607-mpdisposetaskexception)*