# MPSetTaskType

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets the type of the task.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSStatus MPSetTaskType(MPTaskID task, OSType taskType);
```

#### Return Value

The `noErr` result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

This function does nothing and should not be used.

## See Also

### Creating and Scheduling Tasks
- [MPCreateTask](./api-1585779-mpcreatetask.md)
  Creates a preemptive task.
- [MPCurrentTaskID](./api-1585673-mpcurrenttaskid.md)
  Obtains the task ID of the currently-executing preemptive task
- [MPExit](./api-1585705-mpexit.md)
  Allows a task to terminate itself
- [MPGetNextTaskID](./api-1508163-mpgetnexttaskid.md)
  Obtains the next task ID in the list of available tasks.
- [MPSetTaskWeight](./api-1585665-mpsettaskweight.md)
  Assigns a relative weight to a task, indicating how much processor time it should receive compared to other available tasks. 
- [MPTaskIsPreemptive](./api-1585681-mptaskispreemptive.md)
  Determines whether a task is preemptively scheduled. 
- [MPTerminateTask](./api-1585769-mpterminatetask.md)
  Terminates an existing task.
- [MPYield](./api-1585732-mpyield.md)
  Allows a task to yield the processor to another task. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585695-mpsettasktype)*