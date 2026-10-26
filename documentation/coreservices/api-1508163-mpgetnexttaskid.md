# MPGetNextTaskID

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains the next task ID in the list of available tasks.

**Availability**:
- macOS 10.4+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPGetNextTaskID(MPProcessID owningProcessID, MPTaskID *taskID);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

By iterating on this function, you can obtain the IDs of all the tasks in a given process. These tasks may be running, ready, or blocked. Generally you would only use this function in diagnostic programs.  

## Parameters

- `owningProcessID`: The ID of the process (typically the application) that owns the tasks. This ID is the same as the process ID handled by the Code Fragment Manager. 
- `taskID`: On return, `taskID` points to ID of the next task in the list of tasks. 

## See Also

### Creating and Scheduling Tasks
- [MPCreateTask](./api-1585779-mpcreatetask.md)
  Creates a preemptive task.
- [MPCurrentTaskID](./api-1585673-mpcurrenttaskid.md)
  Obtains the task ID of the currently-executing preemptive task
- [MPSetTaskType](./api-1585695-mpsettasktype.md)
  Sets the type of the task.
- [MPExit](./api-1585705-mpexit.md)
  Allows a task to terminate itself
- [MPSetTaskWeight](./api-1585665-mpsettaskweight.md)
  Assigns a relative weight to a task, indicating how much processor time it should receive compared to other available tasks. 
- [MPTaskIsPreemptive](./api-1585681-mptaskispreemptive.md)
  Determines whether a task is preemptively scheduled. 
- [MPTerminateTask](./api-1585769-mpterminatetask.md)
  Terminates an existing task.
- [MPYield](./api-1585732-mpyield.md)
  Allows a task to yield the processor to another task. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1508163-mpgetnexttaskid)*