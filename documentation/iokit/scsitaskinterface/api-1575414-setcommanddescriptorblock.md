# SetCommandDescriptorBlock

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to set the task's SCSICommandDescriptorBlock.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*SetCommandDescriptorBlock)(void *task, UInt8 *inCDB, UInt8 inSize);
```

#### Return Value

Returns kIOReturnSuccess or kIOReturnError.

#### Discussion

This method can be used to set the SCSITasks' SCSICommandDescriptorBlock.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `inCDB`: Pointer to an array of values to be stored in the SCSITask's SCSICommandDescriptorBlock.
- `inSize`: The size of the array inCDB. Valid values are 6, 10, 12, and 16 which have enums defined in SCSITask.h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575414-setcommanddescriptorblock)*