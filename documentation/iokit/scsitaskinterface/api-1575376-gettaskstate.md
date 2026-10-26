# GetTaskState

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the SCSITaskState from the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*GetTaskState)(void *task, SCSITaskState *outState);
```

#### Return Value

Returns kIOReturnSuccess or kIOReturnError.

#### Discussion

This method can be used to get the SCSITaskState from the SCSITask.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `outState`: Pointer to an SCSITaskState.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575376-gettaskstate)*