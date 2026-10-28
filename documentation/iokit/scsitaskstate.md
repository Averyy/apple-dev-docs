# SCSITaskState

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

Attributes for task state.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef enum SCSITaskState : unsigned int {
    ...
} SCSITaskState;
```

## Overview

The Task State represents the current state of the task. The state is set to NEW_TASK when the task is created. The SCSI Protocol Layer will then adjust the state as the task is queued and during execution. The SCSI Application Layer can examine the state to monitor the progress of a task. The Task State can only be modified by the SCSI Protocol Layer. The SCSI Application Layer can only read the state.

## Topics

### Constants
- [kSCSITaskState_NEW_TASK](./scsitaskstate/kscsitaskstate_new_task.md)
- [kSCSITaskState_ENABLED](./scsitaskstate/kscsitaskstate_enabled.md)
- [kSCSITaskState_BLOCKED](./scsitaskstate/kscsitaskstate_blocked.md)
- [kSCSITaskState_DORMANT](./scsitaskstate/kscsitaskstate_dormant.md)
- [kSCSITaskState_ENDED](./scsitaskstate/kscsitaskstate_ended.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskstate)*