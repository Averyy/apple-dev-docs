# GetCommandDescriptorBlock

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the task's SCSICommandDescriptorBlock.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*GetCommandDescriptorBlock)(void *task, UInt8 *outCDB);
```

## Return Value

Returns kIOReturnSucces or kIOReturnError.

## Discussion

This method can be used to get the SCSITasks' SCSICommandDescriptorBlock.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `outCDB`: Pointer to an array the size of the SCSICommandDescriptorBlock in question. Clients should call GetCommandDescriptorBlockSize first to find out how large an array should be passed in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575383-getcommanddescriptorblock)*