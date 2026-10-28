# IsTaskActive

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to find out if the task is active or not.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
Boolean (*IsTaskActive)(void *task);
```

## Return Value

Returns 0 if the task is not active, non-zero if it is active.

## Discussion

Method to find out if the task is active or not. The task is considered "active" if the SCSITaskState is not kSCSITaskState_NEW nor kSCSITaskState_ENDED.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575423-istaskactive)*