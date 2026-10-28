# MPTaskIsPreemptive

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Determines whether a task is preemptively scheduled. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
Boolean MPTaskIsPreemptive(MPTaskID taskID);
```

## Return Value

If true, the task is preemptively scheduled. If false, the task is cooperatively scheduled. 

## Discussion

If you have code that may be called from either cooperative or preemptive tasks, that code can call `MPTaskIsPreemptive` if its actions should differ depending on its execution environment.  

Note that you can call this function from an interrupt handler. 

## Parameters

- `taskID`: The task you want to check. Pass `kMPNoID` or `kInvalidID` if you want to specify the current task. 

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
- [MPGetNextTaskID](./api-1508163-mpgetnexttaskid.md)
  Obtains the next task ID in the list of available tasks.
- [MPSetTaskWeight](./api-1585665-mpsettaskweight.md)
  Assigns a relative weight to a task, indicating how much processor time it should receive compared to other available tasks. 
- [MPTerminateTask](./api-1585769-mpterminatetask.md)
  Terminates an existing task.
- [MPYield](./api-1585732-mpyield.md)
  Allows a task to yield the processor to another task. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585681-mptaskispreemptive)*