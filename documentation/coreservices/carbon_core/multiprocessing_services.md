# Multiprocessing Services

**Framework**: Core Services  
**Role**: API Collection

Support multitasking in your app.

> **Deprecated**: In macOS 10.8 and later, use Grand Central Dispatch (GCD) or POSIX threads instead. For more information, see [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091), the [Dispatch](../../Dispatch/Dispatch.md) framework reference, and [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i).

#### Overview

Multiprocessing Services is an API that lets you create preemptive tasks in your application that can run on one or more microprocessors. Unlike the cooperative threads created by the Thread Manager, Multiprocessing Services automatically divides processor time among the available tasks, so that no particular task can monopolize the system. This document is relevant to you if you want to add multitasking capability to your Mac OS applications.

In macOS, Carbon supports Multiprocessing Services with the following restrictions:

- Debugging functions are not implemented. Use the mach APIs provided by the system to implement debugging services.
- Opaque notification IDs are local to your process; they are not globally addressable across processes.
- Global memory allocation is not supported.

##### Gestalt Constants

You can determine which system software calls are preemptively-safe for Multiprocessing Services by using the preemptive function attribute selectors defined in the Gestalt Manager. For more information, see [Gestalt Manager](./gestalt_manager.md).

## Topics

### Result Codes
- [var kMPIterationEndErr: Int](../kmpiterationenderr.md)
- [var kMPPrivilegedErr: Int](../kmpprivilegederr.md)
- [var kMPProcessCreatedErr: Int](../kmpprocesscreatederr.md)
- [var kMPProcessTerminatedErr: Int](../kmpprocessterminatederr.md)
- [var kMPTaskCreatedErr: Int](../kmptaskcreatederr.md)
- [var kMPTaskBlockedErr: Int](../kmptaskblockederr.md)
  The desired task is blocked.
- [var kMPTaskStoppedErr: Int](../kmptaskstoppederr.md)
  The desired task is stopped.
- [var kMPDeletedErr: Int](../kmpdeletederr.md)
  The desired notification the function was waiting upon was deleted.
- [var kMPTimeoutErr: Int](../kmptimeouterr.md)
  The designated timeout interval passed before the function could take action.
- [var kMPInsufficientResourcesErr: Int](../kmpinsufficientresourceserr.md)
  Could not complete task due to unavailable Multiprocessing Services resources. Note that many functions return this value as a general error when the desired action could not be performed.
- [var kMPInvalidIDErr: Int](../kmpinvalididerr.md)
  Invalid ID value. For example, an invalid message queue ID was passed to `MPNotifyQueue`.
- [kMPIterationEndErr](../api-1560027-anonymous/kmpiterationenderr.md)
- [kMPPrivilegedErr](../api-1560027-anonymous/kmpprivilegederr.md)
- [kMPProcessCreatedErr](../api-1560027-anonymous/kmpprocesscreatederr.md)
- [kMPProcessTerminatedErr](../api-1560027-anonymous/kmpprocessterminatederr.md)
- [kMPTaskCreatedErr](../api-1560027-anonymous/kmptaskcreatederr.md)
- [kMPTaskBlockedErr](../api-1560027-anonymous/kmptaskblockederr.md)
  The desired task is blocked.
- [kMPTaskStoppedErr](../api-1560027-anonymous/kmptaskstoppederr.md)
  The desired task is stopped.
- [kMPDeletedErr](../api-1560027-anonymous/kmpdeletederr.md)
  The desired notification the function was waiting upon was deleted.
- [kMPTimeoutErr](../api-1560027-anonymous/kmptimeouterr.md)
  The designated timeout interval passed before the function could take action.
- [kMPInsufficientResourcesErr](../api-1560027-anonymous/kmpinsufficientresourceserr.md)
  Could not complete task due to unavailable Multiprocessing Services resources. Note that many functions return this value as a general error when the desired action could not be performed.
- [kMPInvalidIDErr](../api-1560027-anonymous/kmpinvalididerr.md)
  Invalid ID value. For example, an invalid message queue ID was passed to `MPNotifyQueue`.
### Determining Multiprocessing Services And Processor Availability
- [_MPIsFullyInitialized](./multiprocessing_services/api-1809315-_mpisfullyinitialized.md)
  Indicates whether Multiprocessing Services is available for use.
- [MPGetNextCpuID](../api-1508189-mpgetnextcpuid.md)
  Obtains the next CPU ID in the list of physical processors of the specified memory coherence group. 
- [MPProcessors](../api-1585778-mpprocessors.md)
  Returns the number of processors on the host computer. 
- [MPProcessorsScheduled](../api-1585777-mpprocessorsscheduled.md)
  Returns the number of active processors available on the host computer. 
### Creating and Handling Message Queues
- [MPCreateQueue](../api-1585694-mpcreatequeue.md)
  Creates a message queue.
- [MPDeleteQueue](../api-1585571-mpdeletequeue.md)
  Deletes a message queue.
- [MPNotifyQueue](../api-1585699-mpnotifyqueue.md)
  Sends a message to the specified message queue.
- [MPSetQueueReserve](../api-1585671-mpsetqueuereserve.md)
  Reserves space for messages on a specified message queue. 
- [MPWaitOnQueue](../api-1585762-mpwaitonqueue.md)
  Obtains a message from a specified message queue. 
### Creating and Handling Semaphores
- [MPCreateSemaphore](../api-1585569-mpcreatesemaphore.md)
  Creates a semaphore.
- [MPDeleteSemaphore](../api-1585586-mpdeletesemaphore.md)
  Removes a semaphore. 
- [MPSignalSemaphore](../api-1585713-mpsignalsemaphore.md)
  Signals a semaphore. 
- [MPWaitOnSemaphore](../api-1585722-mpwaitonsemaphore.md)
  Waits on a semaphore
### Creating and Scheduling Tasks
- [MPCreateTask](../api-1585779-mpcreatetask.md)
  Creates a preemptive task.
- [MPCurrentTaskID](../api-1585673-mpcurrenttaskid.md)
  Obtains the task ID of the currently-executing preemptive task
- [MPSetTaskType](../api-1585695-mpsettasktype.md)
  Sets the type of the task.
- [MPExit](../api-1585705-mpexit.md)
  Allows a task to terminate itself
- [MPGetNextTaskID](../api-1508163-mpgetnexttaskid.md)
  Obtains the next task ID in the list of available tasks.
- [MPSetTaskWeight](../api-1585665-mpsettaskweight.md)
  Assigns a relative weight to a task, indicating how much processor time it should receive compared to other available tasks. 
- [MPTaskIsPreemptive](../api-1585681-mptaskispreemptive.md)
  Determines whether a task is preemptively scheduled. 
- [MPTerminateTask](../api-1585769-mpterminatetask.md)
  Terminates an existing task.
- [MPYield](../api-1585732-mpyield.md)
  Allows a task to yield the processor to another task. 
### Handling Critical Regions
- [MPCreateCriticalRegion](../api-1585663-mpcreatecriticalregion.md)
  Creates a critical region object.
- [MPDeleteCriticalRegion](../api-1585704-mpdeletecriticalregion.md)
  Removes the specified critical region object. 
- [MPEnterCriticalRegion](../api-1585622-mpentercriticalregion.md)
  Attempts to enter a critical region. 
- [MPExitCriticalRegion](../api-1585758-mpexitcriticalregion.md)
  Exits a critical region. 
### Handling Event Groups
- [MPCreateEvent](../api-1585702-mpcreateevent.md)
  Creates an event group.
- [MPDeleteEvent](../api-1585691-mpdeleteevent.md)
  Removes an event group. 
- [MPSetEvent](../api-1585752-mpsetevent.md)
  Merges event flags into a specified event group. 
- [MPWaitForEvent](../api-1585656-mpwaitforevent.md)
  Retrieves event flags from a specified event group. 
### Handling Kernel Notifications
- [MPCauseNotification](../api-1585754-mpcausenotification.md)
  Signals a kernel notification. 
- [MPCreateNotification](../api-1585723-mpcreatenotification.md)
  Creates a kernel notification
- [MPDeleteNotification](../api-1585659-mpdeletenotification.md)
  Removes a kernel notification. 
- [MPModifyNotification](../api-1585780-mpmodifynotification.md)
  Adds a simple notification to a kernel notification.
- [MPModifyNotificationParameters](../api-1585668-mpmodifynotificationparameters.md)
### Accessing Per-Task Storage Variables
- [MPAllocateTaskStorageIndex](../api-1585719-mpallocatetaskstorageindex.md)
  Returns an index number to access per-task storage. 
- [MPDeallocateTaskStorageIndex](../api-1585649-mpdeallocatetaskstorageindex.md)
  Frees an index number used to access per-task storage 
- [MPGetTaskStorageValue](../api-1585589-mpgettaskstoragevalue.md)
  Gets the storage value stored at a specified index number. 
- [MPSetTaskStorageValue](../api-1585626-mpsettaskstoragevalue.md)
  Sets the storage value for a given index number. 
### Memory Allocation Functions
- [MPAllocate](../api-1585756-mpallocate.md)
  Allocates a nonrelocatable memory block.
- [MPAllocateAligned](../api-1585774-mpallocatealigned.md)
  Allocates a nonrelocatable memory block.
- [MPBlockClear](../api-1585642-mpblockclear.md)
  Clears a block of memory. 
- [MPBlockCopy](../api-1585707-mpblockcopy.md)
  Copies a block of memory.
- [MPFree](../api-1585676-mpfree.md)
  Frees memory allocated by `MPAllocateAligned`. 
- [MPGetAllocatedBlockSize](../api-1585717-mpgetallocatedblocksize.md)
  Returns the size of a memory block.
### Remote Calling Functions
- [MPRemoteCall](../api-1585652-mpremotecall.md)
  Calls a non-reentrant function and blocks the current task. 
- [MPRemoteCallCFM](../api-1585757-mpremotecallcfm.md)
  Calls a non-reentrant function and blocks the current task. 
### Timer Services Functions
- [MPArmTimer](../api-1585612-mparmtimer.md)
  Arms the timer to expire at a given time. 
- [MPCancelTimer](../api-1585745-mpcanceltimer.md)
  Cancels an armed timer. 
- [MPCreateTimer](../api-1585748-mpcreatetimer.md)
  Creates a timer.
- [MPDelayUntil](../api-1585647-mpdelayuntil.md)
  Blocks the calling task until a specified time. 
- [MPDeleteTimer](../api-1585761-mpdeletetimer.md)
  Removes a timer. 
- [MPSetTimerNotify](../api-1585726-mpsettimernotify.md)
  Sets the notification information associated with a timer. 
### Exception Handling Functions
- [MPDisposeTaskException](../api-1585607-mpdisposetaskexception.md)
  Removes a task exception.
- [MPExtractTaskState](../api-1585718-mpextracttaskstate.md)
  Extracts state information from a suspended task.
- [MPSetExceptionHandler](../api-1585759-mpsetexceptionhandler.md)
  Sets an exception handler for a task. 
- [MPSetTaskState](../api-1585601-mpsettaskstate.md)
  Sets state information for a suspended task. 
- [MPThrowException](../api-1585743-mpthrowexception.md)
  Throws an exception to a specified task.
### Debugger Support Functions
- [MPRegisterDebugger](../api-1585573-mpregisterdebugger.md)
  Registers a debugger. 
- [MPUnregisterDebugger](../api-1585598-mpunregisterdebugger.md)
  Unregisters a debugger. 
### Callbacks
- [MPRemoteProcedure](../mpremoteprocedure.md)
  Defines a remote procedure call.
- [TaskProc](../taskproc.md)
  Defines the entry point of a task.
### Data Types
- [MPAddressSpaceID](../mpaddressspaceid.md)
- [MPAddressSpaceInfo](../mpaddressspaceinfo.md)
- [MPAreaID](../mpareaid.md)
- [MPCoherenceID](../mpcoherenceid.md)
  Represents a memory coherence group. 
- [MPConsoleID](../mpconsoleid.md)
- [MPCpuID](../mpcpuid.md)
  Represents a CPU ID.
- [MPCriticalRegionID](../mpcriticalregionid.md)
  Represents a critical region ID, which Multiprocessing Services uses to manipulate critical regions. 
- [MPCriticalRegionInfo](../mpcriticalregioninfo.md)
- [MPEventFlags](../mpeventflags.md)
  Represents event information for an event group. 
- [MPEventID](../mpeventid.md)
  Represents an event group ID, which Multiprocessing Services uses to manipulate event groups.
- [MPEventInfo](../mpeventinfo.md)
- [MPExceptionKind](../mpexceptionkind.md)
  Represents the kind of exception thrown. 
- [MPNotificationID](../mpnotificationid.md)
  Represents a notification ID, which Multiprocessing Services uses to manipulate kernel notifications.
- [MPNotificationInfo](../mpnotificationinfo.md)
- [MPOpaqueID](../mpopaqueid.md)
  Represents a generic notification ID (that is, an ID that could be a queue ID, event ID, kernel notification ID, or semaphore ID). 
- [MPOpaqueIDClass](../mpopaqueidclass.md)
- [MPPageSizeClass](../mppagesizeclass.md)
- [MPProcessID](../mpprocessid.md)
  Represents a process ID. 
- [MPQueueID](../mpqueueid.md)
  Represents a queue ID, which Multiprocessing Services uses to manipulate message queues.
- [MPQueueInfo](../mpqueueinfo.md)
- [MPSemaphoreCount](../mpsemaphorecount.md)
  Represents a semaphore count. 
- [MPSemaphoreID](../mpsemaphoreid.md)
  Represents a semaphore ID, which Multiprocessing Services uses to manipulate semaphores.
- [MPSemaphoreInfo](../mpsemaphoreinfo.md)
- [MPTaskID](../mptaskid.md)
  Represents a task ID. 
- [MPTaskInfo](../mptaskinfo.md)
  Contains information about a task. 
- [MPTaskInfoVersion2](../mptaskinfoversion2.md)
- [MPTaskStateKind](../mptaskstatekind.md)
- [MPTaskWeight](../mptaskweight.md)
  Represents the relative processor weighting of a task. 
- [MPTimerID](../mptimerid.md)
  Represents a timer ID. 
- [TaskStorageIndex](../taskstorageindex.md)
  Represents a task storage index value used by functions described in “Accessing Per-Task Storage Variables.”
- [TaskStorageValue](../taskstoragevalue.md)
  Represents a task storage value used by functions described in “Accessing Per-Task Storage Variables.”
### Constants
- [Allocation constants](../api-1585776-allocation_constants.md)
  The maximum memory allocation size.
- [Task IDs](../api-1585747-task_ids.md)
  Use to specify no task ID. 
- [Data Structure Version Constants](../api-1508102-data_structure_version_constants.md)
  Data structure version information constants.
- [Values for the MPOpaqueIDClass type](../api-1585638-values_for_the_mpopaqueidclass_t.md)
  Constants indicating the source of a generic notification.
- [Memory Allocation Alignment Constants](../api-1585698-memory_allocation_alignment_cons.md)
  Specify the alignment of the desired memory block when calling the `MPAllocateAligned` function.
- [Memory Allocation Option Constants](../api-1585664-memory_allocation_option_constan.md)
  Specify optional actions when calling the `MPAllocateAligned` function. 
- [MPDebuggerLevel](../mpdebuggerlevel.md)
  Indicates the debugger level. 
- [Library Version Constants](../api-1585672-library_version_constants.md)
  Identifies the current library version.
- [MPRemoteContext](../mpremotecontext.md)
  Specify which contexts are allowed to execute the callback function when using `MPRemoteCall`.
- [MPTaskOptions](../mptaskoptions.md)
  Specify optional actions when calling the `MPCreateTask` function.
- [Task Exception Disposal Constants](../api-1585628-task_exception_disposal_constant.md)
  Specify actions to take on an exception when passed in the `action` parameter of the `MPDisposeTaskException` function.
- [Task Information Structure Version Constant](../api-1585620-task_information_structure_versi.md)
  Indicates the current version of the `MPTaskInfo` structure (returned as the first field). 
- [Task Run State Constants](../api-1585643-task_run_state_constants.md)
  Indicate the state of the task when returned as part of the `MPTaskInfo` data structure. 
- [Task State Constants](../api-1585773-task_state_constants.md)
  Specify what states you want to set or obtain when calling the `MPExtractTaskState` or `MPSetTaskState` functions. 
- [Timer Duration Constants](../api-1585641-timer_duration_constants.md)
  Specify the maximum time a task should wait for an event to occur. 
- [Timer Option Masks](../api-1585611-timer_option_masks.md)
  Indicate optional actions when calling `MPArmTimer`. 

## See Also

### Services
- [Debugger Services](./debugger_services.md)
  Handle assertions and exceptions at run time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/multiprocessing_services)*