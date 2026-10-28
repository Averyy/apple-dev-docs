# MPSetTaskWeight

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Assigns a relative weight to a task, indicating how much processor time it should receive compared to other available tasks. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPSetTaskWeight(MPTaskID task, MPTaskWeight weight);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

The approximate processor share is defined as:

```occ
weight of the task / total weight of available tasks
```

For a set of ready tasks, the amount of CPU time dedicated to the tasks will be determined by the dynamically computed share. Note that the processor share devoted to tasks may deviate from the suggested weighting if critical tasks require attention. For example, a real-time task (such as a QuickTime movie) may require more than its relative weight of processor time, and the scheduler will adjust proportions accordingly.  

## Parameters

- `task`: The ID of the task to which you want to assign a weighting. 
- `weight`: The relative weight to assign. This value can range from 1 to 10,000, with the default value being 100. 

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
- [MPTaskIsPreemptive](./api-1585681-mptaskispreemptive.md)
  Determines whether a task is preemptively scheduled. 
- [MPTerminateTask](./api-1585769-mpterminatetask.md)
  Terminates an existing task.
- [MPYield](./api-1585732-mpyield.md)
  Allows a task to yield the processor to another task. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585665-mpsettaskweight)*