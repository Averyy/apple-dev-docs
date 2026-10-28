# ResetForNewTask

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to reset the SCSITask to defaults.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ResetForNewTask)(void *task);
```

## Return Value

Returns kIOReturnSuccess if reset was successful, otherwise kIOReturnError.

## Discussion

This method can be used to reset the SCSITask to defaults.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575364-resetfornewtask)*