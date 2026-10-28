# Workgroups

**Framework**: os  
**Role**: API Collection

Schedule one or more threads to run at regular intervals and before specific deadlines.

## Overview

A workgroup manages one or more threads that work cooperatively toward a common goal. Use workgroups to coordinate the efforts of threads that handle real-time audio work. Registering threads with a workgroup helps the system direct work to the right system resources, and also helps it manage the competing needs of low-power consumption with maximum rendering output.

## Topics

### Essentials
- [Tuning your code’s performance for Apple silicon](../apple-silicon/tuning-your-code-s-performance-for-apple-silicon.md)
  Improve your code to get the best performance from both Apple silicon and Intel-based Mac computers.
### Interval Tasks
- [Porting your audio code to Apple silicon](../apple-silicon/porting-your-audio-code-to-apple-silicon.md)
  Eliminate issues in your audio-specific code when running on Apple silicon Mac computers.
- [os_workgroup_interval_start](./os_workgroup_interval_start.md)
  Starts the regular execution of the workgroup’s threads at the specified time.
- [os_workgroup_interval_update](./os_workgroup_interval_update.md)
  Schedules a new deadline for workgroup threads that run at regular intervals.
- [os_workgroup_interval_finish](./os_workgroup_interval_finish.md)
  Stops the current interval-based execution of the workgroup’s threads.
- [os_workgroup_interval_t](./os_workgroup_interval_t.md)
  A workgroup object that supports the scheduling of threads on a repeating cadence.
- [os_workgroup_interval_data_t](./os_workgroup_interval_data_t.md)
  An opaque structure that contains additional configuration data for the interval workgroup.
- [os_clockid_t](./os_clockid_t.md)
  Options for how to specify time-specific values in an interval workgroup.
### Parallel
- [os_workgroup_parallel_create](./os_workgroup_parallel_create.md)
  Creates a new workgroup that manges threads working on a single task in parallel.
- [os_workgroup_parallel_t](./os_workgroup_parallel_t.md)
  A workgroup object that supports the scheduling of threads that work in parallel to complete a task.
### Thread Attachment
- [os_workgroup_join](./os_workgroup_join.md)
  Adds the current thread to the specified workgroup.
- [os_workgroup_leave](./os_workgroup_leave.md)
  Removes the current thread from the workgroup it previously joined.
- [os_workgroup_join_token_t](./os_workgroup_join_token_t.md)
  An opaque token that represents a connection between a thread and a workgroup.
### Cancellation
- [os_workgroup_cancel](./os_workgroup_cancel.md)
  Cancels and invalidates the specified workgroup.
- [os_workgroup_testcancel](./os_workgroup_testcancel.md)
  Returns a Boolean value that indicates whether the workgroup is canceled.
### Workgroup Configuration
- [os_workgroup_max_parallel_threads](./os_workgroup_max_parallel_threads.md)
  Returns the maximum number of threads that the system recommends you add to the specified workgroup.
- [os_workgroup_mpt_attr_t](./os_workgroup_mpt_attr_t.md)
  An opaque structure containing attributes related to a request for the maximum number of parallel threads.
- [os_workgroup_set_working_arena](./os_workgroup_set_working_arena.md)
  Distributes a block of managed memory to the threads of a workgroup.
- [os_workgroup_get_working_arena](./os_workgroup_get_working_arena.md)
  Retrieves the workgroup’s shared data, and the thread-specific index into that data.
- [os_workgroup_index](./os_workgroup_index.md)
  A unique index that the workgroup assigns to its joined threads.
- [os_workgroup_working_arena_destructor_t](./os_workgroup_working_arena_destructor_t.md)
  A function that deallocates a workgroup’s currently assigned shared memory.
### Common Utilities
- [os_workgroup_create_with_workgroup](./os_workgroup_create_with_workgroup.md)
  Create a new workgroup that is bound to the specified workgroup.
- [os_workgroup_create_with_port](./os_workgroup_create_with_port.md)
  Creates a new workgroup that is bound to the workgroup with the specified Mach port.
- [os_workgroup_copy_port](./os_workgroup_copy_port.md)
  Returns the Mach port associated with the workgroup.
- [os_workgroup_t](./os_workgroup_t.md)
  An opaque object representing a default workgroup in the current process.
- [os_workgroup_attr_t](./os_workgroup_attr_t.md)
  An opaque structure for storing workgroup-related attributes.
### Objective-C Support
- [OS_os_workgroup_interval](./os_os_workgroup_interval-c.class.md)
- [OS_os_workgroup_interval](./os_os_workgroup_interval-c.protocol.md)
- [OS_os_workgroup](./os_os_workgroup.md)
- [OS_object](./os_object.md)
### Internal Structures
- [OS_os_workgroup_parallel](./os_os_workgroup_parallel-c.class.md)
- [OS_os_workgroup_parallel](./os_os_workgroup_parallel-c.protocol.md)

## See Also

### Task Management
- [Synchronization](./synchronization.md)
  Access low-level synchronization mechanisms to control state across threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/workgroups)*