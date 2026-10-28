# GetTaskAttribute

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the task's attribute.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*GetTaskAttribute)(void *task, SCSITaskAttribute *outAttribute);
```

## Return Value

Returns kIOReturnSuccess or kIOReturnError.

## Discussion

This method can be used to get the SCSITasks' SCSITaskAttribute field. Valid values are defined in SCSITask.h

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `outAttribute`: Pointer to the attribute value stored in the SCSITask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575401-gettaskattribute)*