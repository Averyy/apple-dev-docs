# os_workgroup_interval_data_t

**Framework**: os  
**Kind**: typealias  
**Role**: Type Alias

An opaque structure that contains additional configuration data for the interval workgroup.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef struct os_workgroup_interval_data_opaque_s * os_workgroup_interval_data_t;
```

## See Also

### Interval Tasks
- [os_workgroup_interval_start](./os_workgroup_interval_start.md)
  Starts the regular execution of the workgroup’s threads at the specified time.
- [os_workgroup_interval_update](./os_workgroup_interval_update.md)
  Schedules a new deadline for workgroup threads that run at regular intervals.
- [os_workgroup_interval_finish](./os_workgroup_interval_finish.md)
  Stops the current interval-based execution of the workgroup’s threads.
- [os_workgroup_interval_t](./os_workgroup_interval_t.md)
  A workgroup object that supports the scheduling of threads on a repeating cadence.
- [os_clockid_t](./os_clockid_t.md)
  Options for how to specify time-specific values in an interval workgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_interval_data_t)*