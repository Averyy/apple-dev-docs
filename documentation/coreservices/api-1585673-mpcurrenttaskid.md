# MPCurrentTaskID

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains the task ID of the currently-executing preemptive task

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
MPTaskID MPCurrentTaskID(void);
```

## Return Value

The task ID of the current preemptive task. See the description of the `MPTaskID` data type.

## Discussion

Returns the ID of the current preemptive task. If called from a cooperative task, this function returns an ID which is different than the ID of any preemptive task. Nonpreemptive processes may or may not have different task IDs for each application; future implementations of this API may behave differently in this regard.

Note that you can call this function from an interrupt handler. 

## See Also

### Creating and Scheduling Tasks
- [MPCreateTask](./api-1585779-mpcreatetask.md)
  Creates a preemptive task.
- [MPSetTaskType](./api-1585695-mpsettasktype.md)
  Sets the type of the task.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585673-mpcurrenttaskid)*