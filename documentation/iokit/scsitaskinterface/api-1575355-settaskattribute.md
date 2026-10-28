# SetTaskAttribute

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to set the task's attribute.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*SetTaskAttribute)(void *task, SCSITaskAttribute inAttribute);
```

## Return Value

Returns kIOReturnSuccess or kIOReturnError.

## Discussion

This method can be used to set the SCSITask's SCSITaskAttribute field. Valid values are defined in SCSITask.h

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `inAttribute`: The new attribute value to be stored in the SCSITask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575355-settaskattribute)*