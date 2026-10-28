# MPExit

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows a task to terminate itself

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
void MPExit(OSStatus status);
```

## Discussion

When called from within a preemptive task, the task terminates, and the value indicated by the parameter `status` is sent to the termination message queue you specified in  [`MPCreateTask`](./api-1585779-mpcreatetask.md). Note that you cannot call `MPExit` from outside a preemptive task. 

## Parameters

- `status`: An application-defined value that indicates termination status. This value is sent to the termination message queue in place of the task’s result code. 

## See Also

### Creating and Scheduling Tasks
- [MPCreateTask](./api-1585779-mpcreatetask.md)
  Creates a preemptive task.
- [MPCurrentTaskID](./api-1585673-mpcurrenttaskid.md)
  Obtains the task ID of the currently-executing preemptive task
- [MPSetTaskType](./api-1585695-mpsettasktype.md)
  Sets the type of the task.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585705-mpexit)*