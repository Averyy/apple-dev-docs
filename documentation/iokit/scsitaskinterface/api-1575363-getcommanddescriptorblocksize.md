# GetCommandDescriptorBlockSize

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the task's SCSICommandDescriptorBlock size.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
UInt8 (*GetCommandDescriptorBlockSize)(void *task);
```

#### Return Value

UInt8 which is the size of the SCSICommandDescriptorBlock. Valid values are 6, 10, 12, and 16 which have enums defined in SCSITask.h

#### Discussion

This method can be used to get the size of the SCSITask's SCSICommandDescriptorBlock.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575363-getcommanddescriptorblocksize)*