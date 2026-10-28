# os_workgroup_interval_update

**Framework**: os  
**Kind**: func  
**Role**: Function

Schedules a new deadline for workgroup threads that run at regular intervals.

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
extern int os_workgroup_interval_update(os_workgroup_interval_t wg, uint64_t deadline, os_workgroup_interval_data_t data);
```

## Return Value

A value of `0` on success, or a nonzero error code indicating why the function failed. Common error codes include `EINVAL` or `EPERM`. For example, this method returns `EINVAL` if you didn’t start the workgroup.

## Discussion

Call this function between calls to the [`os_workgroup_interval_start`](./os_workgroup_interval_start.md) and [`os_workgroup_interval_finish`](./os_workgroup_interval_finish.md) functions. Typically, you call it at regular intervals to set a new deadline for any ongoing work. For example, after delivering content for the current video frame, call this function to set the deadline for finishing the next video frame. Call this function only once for each new interval. If your workgroup contains multiple threads, designate one thread to start, stop, and update the group.

This function returns an error if you created the workgroup using the [`os_workgroup_create_with_workgroup`](./os_workgroup_create_with_workgroup.md) or [`os_workgroup_create_with_port`](./os_workgroup_create_with_port.md) function. This function works only on workgroups that you create using the `os_workgroup_interval_create` function.

## Parameters

- `wg`: A workgroup containing one or more threads, including the current thread. If the current thread is not part of this workgroup, this function aborts the process.
- `deadline`: The ideal time at which you expect the threads to complete the task for the current interval. The system uses this parameter to assess whether your threads finish early, on-time, or later than expected. Specify this value using the time units of the workgroup. For a list of possible time units, see [`os_clockid_t`](./os_clockid_t.md). This value must be greater than the value in the `start` parameter.
- `data`: Additional interval data. Specify `NULL` for this parameter.

## See Also

### Interval Tasks
- [os_workgroup_interval_start](./os_workgroup_interval_start.md)
  Starts the regular execution of the workgroup’s threads at the specified time.
- [os_workgroup_interval_finish](./os_workgroup_interval_finish.md)
  Stops the current interval-based execution of the workgroup’s threads.
- [os_workgroup_interval_t](./os_workgroup_interval_t.md)
  A workgroup object that supports the scheduling of threads on a repeating cadence.
- [os_workgroup_interval_data_t](./os_workgroup_interval_data_t.md)
  An opaque structure that contains additional configuration data for the interval workgroup.
- [os_clockid_t](./os_clockid_t.md)
  Options for how to specify time-specific values in an interval workgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_interval_update)*