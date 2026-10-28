# os_workgroup_interval_finish

**Framework**: os  
**Kind**: func  
**Role**: Function

Stops the current interval-based execution of the workgroup’s threads.

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
extern int os_workgroup_interval_finish(os_workgroup_interval_t wg, os_workgroup_interval_data_t data);
```

## Return Value

A value of `0` on success, or a nonzero error code indicating why the function failed. Common error codes include `EINVAL` or `EPERM`. For example, this method returns `EINVAL` if you didn’t start the workgroup.

## Discussion

Call this function when you no longer need your workgroup’s threads to run at regular intervals. For example, call this function when the user’s video finishes playing and you no longer need to decode the video frames. This function puts the workgroup back into the idle state, from which you can start it again by calling the [`os_workgroup_interval_start`](./os_workgroup_interval_start.md) function.

This function returns an error if you created the workgroup using the [`os_workgroup_create_with_workgroup`](./os_workgroup_create_with_workgroup.md) or [`os_workgroup_create_with_port`](./os_workgroup_create_with_port.md) function. This function works only on workgroups that you create using the `os_workgroup_interval_create` function.

## Parameters

- `wg`: A workgroup containing one or more threads, including the current thread. If the current thread is not part of this workgroup, this function aborts the process.
- `data`: Additional interval data. Specify `NULL` for this parameter.

## See Also

### Interval Tasks
- [os_workgroup_interval_start](./os_workgroup_interval_start.md)
  Starts the regular execution of the workgroup’s threads at the specified time.
- [os_workgroup_interval_update](./os_workgroup_interval_update.md)
  Schedules a new deadline for workgroup threads that run at regular intervals.
- [os_workgroup_interval_t](./os_workgroup_interval_t.md)
  A workgroup object that supports the scheduling of threads on a repeating cadence.
- [os_workgroup_interval_data_t](./os_workgroup_interval_data_t.md)
  An opaque structure that contains additional configuration data for the interval workgroup.
- [os_clockid_t](./os_clockid_t.md)
  Options for how to specify time-specific values in an interval workgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_interval_finish)*