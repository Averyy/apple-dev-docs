# MPYield

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows a task to yield the processor to another task. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
void MPYield(void);
```

## Discussion

This function indicates to the scheduler that another task can run. Other than possibly yielding the processor to another task or application, the call has no effect. Note that since tasks are preemptively scheduled, an implicit yield may occur at any point, whether or not this function is called. 

In most cases you should not need to call this function. The most common use of `MPYield` is to release the processor when a task is in a loop in which further progress is dependent on other tasks, and the task cannot be blocked by waiting on a Multiprocessing Services resource. You should avoid such busy waiting whenever possible.

Note that you can call this function from an interrupt handler. 

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
- [MPTaskIsPreemptive](./api-1585681-mptaskispreemptive.md)
  Determines whether a task is preemptively scheduled. 
- [MPTerminateTask](./api-1585769-mpterminatetask.md)
  Terminates an existing task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585732-mpyield)*