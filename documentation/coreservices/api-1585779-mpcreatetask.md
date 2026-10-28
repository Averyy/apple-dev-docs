# MPCreateTask

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a preemptive task.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCreateTask(TaskProc entryPoint, void *parameter, ByteCount stackSize, MPQueueID notifyQueue, void *terminationParameter1, void *terminationParameter2, MPTaskOptions options, MPTaskID *task);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If `MPCreateTask` could not create the task because some critical resource was not available, the function returns `kMPInsufficientResourcesErr`. Usually this is due to lack of memory to allocate the internal data structures associated with the task or the stack. The function also returns `kMPInsufficientResourcesErr` if any reserved option bits are set.

## Discussion

Tasks are created in the unblocked state, ready for execution. A task can terminate in the following ways:

-  By returning from its entry point 
-  By calling  [`MPExit`](./api-1585705-mpexit.md)
-  When specified as the target of an  [`MPTerminateTask`](./api-1585769-mpterminatetask.md)  call 
-  If a hardware-detected exception or programming exception occurs and no exception handler is installed  
-  If the application calls `ExitToShell `

Task resources (its stack, active timers, internal structures related to the task, and so on) are reclaimed by the system when the task terminates. The task's address space is inherited from the process address space. All existing tasks are terminated when the owning process terminates.

To set the relative processor weight to be assigned to a task, use the function  [`MPSetTaskWeight`](./api-1585665-mpsettaskweight.md).

See also the function  [`MPTerminateTask`](./api-1585769-mpterminatetask.md). 

## Parameters

- `entryPoint`: A pointer to the task function. The task function should take a single pointer-sized parameter and return a value of type `OSStatus`.
- `parameter`: The parameter to pass to the task function. 
- `stackSize`: The size of the stack assigned to the task. Note that you should be careful not to exceed the bounds of the stack, since stack overflows may not be detected. Specifying zero for the size will result in a default stack size of 4KB. 

  Note that in macOS prior to version 10.1, this parameter is ignored, and all stacks have the default size of 512 KB. Versions 10.1 and later do not have this limitation.
- `notifyQueue`: The ID of the message queue to which the system will send a message when the task terminates. You specify the first two values of the message in the parameters `terminationParameter1` and `terminationParameter2` respectively. The last message value contains the result code of the task function.
- `terminationParameter1`: A pointer-sized value that is sent to the message queue specified by the parameter `notifyQueue` when the task terminates.
- `terminationParameter2`: A pointer-sized value that is sent to the message queue specified by the parameter `notifyQueue` when the task terminates.
- `options`: Optional attributes of the preemptive task. See [`MPTaskOptions`](./mptaskoptions.md) for a list of possible values. 
- `task`: On return, `task` points to the ID of the newly created task. 

## See Also

### Creating and Scheduling Tasks
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
- [MPYield](./api-1585732-mpyield.md)
  Allows a task to yield the processor to another task. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585779-mpcreatetask)*