# os_workgroup_interval_start

**Framework**: os  
**Kind**: func  
**Role**: Function

Starts the regular execution of the workgroup’s threads at the specified time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```c
extern int os_workgroup_interval_start(os_workgroup_interval_t wg, uint64_t start, uint64_t deadline, os_workgroup_interval_data_t data);
```

## Return Value

A value of `0` on success, or a nonzero error code indicating why the function failed. Common error codes include `EINVAL` or `EPERM`. For example, this method returns `EINVAL` if you previously started or canceled the workgroup.

## Discussion

Join all threads to the workgroup before calling this function, and start each thread working on the target task. Call this function from only one of the threads to mark the start of the task and to set the target deadline. When your threads finish the current task, call [`os_workgroup_interval_update`](./os_workgroup_interval_update.md) to begin the next interval-based task. When the threads finish with the overall task, call [`os_workgroup_interval_finish`](./os_workgroup_interval_finish.md) to let the system know that your threads are done with their interval-based work.

You must balance each call to this function with a call to [`os_workgroup_interval_finish`](./os_workgroup_interval_finish.md) at some point. In between, you may call [`os_workgroup_interval_update`](./os_workgroup_interval_update.md) as many times as you like to update the current interval deadline. For example, you might call [`os_workgroup_interval_update`](./os_workgroup_interval_update.md) at least once every 16.6 milliseconds when decoding video for playback.

This function returns an error if you created the workgroup using the [`os_workgroup_create_with_workgroup`](./os_workgroup_create_with_workgroup.md) or [`os_workgroup_create_with_port`](./os_workgroup_create_with_port.md) function. This function works only on workgroups that you create using the `os_workgroup_interval_create` function.

## Parameters

- `wg`: A workgroup containing one or more threads, including the current thread. If the current thread is not part of this workgroup, this function aborts the process.
- `start`: The time at which your thread started the work associated with the current deadline. Specify this value using the time units of the workgroup. For a list of possible time units, see [`os_clockid_t`](./os_clockid_t.md).
- `deadline`: The ideal time at which you expect the threads to complete the task for the current interval. The system uses this parameter to assess whether your threads finish early, on-time, or later than expected. Specify this value using the time units of the workgroup. For a list of possible time units, see [`os_clockid_t`](./os_clockid_t.md). This value must be greater than the value in the `start` parameter.
- `data`: Additional interval data. Specify `NULL` for this parameter.

## See Also

### Interval Tasks
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_interval_start)*