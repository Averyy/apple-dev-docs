# GetTaskStatus

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the SCSITaskStatus from the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*GetTaskStatus)(void *task, SCSITaskStatus *outStatus);
```

## Return Value

Returns kIOReturnSuccess or kIOReturnError.

## Discussion

This method can be used to get the SCSITaskStatus from the SCSITask.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `outStatus`: Pointer to an SCSITaskStatus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575357-gettaskstatus)*