# Task Exception Disposal Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify actions to take on an exception when passed in the `action` parameter of the `MPDisposeTaskException` function.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kMPTaskPropagate](./api-1585628-task_exception_disposal_constant/kmptaskpropagate.md)
- [kMPTaskResumeStep](./api-1585628-task_exception_disposal_constant/kmptaskresumestep.md)
- [kMPTaskResumeBranch](./api-1585628-task_exception_disposal_constant/kmptaskresumebranch.md)
- [kMPTaskResumeMask](./api-1585628-task_exception_disposal_constant/kmptaskresumemask.md)
  Resume the task.
- [kMPTaskPropagateMask](./api-1585628-task_exception_disposal_constant/kmptaskpropagatemask.md)
  Propagate the exception to the next debugger level.
- [kMPTaskResumeStepMask](./api-1585628-task_exception_disposal_constant/kmptaskresumestepmask.md)
  Resume the task and enable single stepping.
- [kMPTaskResumeBranchMask](./api-1585628-task_exception_disposal_constant/kmptaskresumebranchmask.md)
  Resume the task and enable branch stepping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585628-task_exception_disposal_constant)*