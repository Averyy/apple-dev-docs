# MPTaskOptions

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Specify optional actions when calling the `MPCreateTask` function.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef OptionBits MPTaskOptions;
```

## Topics

### Constants
- [kMPCreateTaskSuspendedMask](./api-1585581-anonymous/kmpcreatetasksuspendedmask.md)
- [kMPCreateTaskTakesAllExceptionsMask](./api-1585581-anonymous/kmpcreatetasktakesallexceptionsmask.md)
  The task will take all exceptions, including those normally handled by the system, such as page faults.
- [kMPCreateTaskNotDebuggableMask](./api-1585581-anonymous/kmpcreatetasknotdebuggablemask.md)
- [kMPCreateTaskValidOptionsMask](./api-1585581-anonymous/kmpcreatetaskvalidoptionsmask.md)
  Include all valid options for this task. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mptaskoptions)*