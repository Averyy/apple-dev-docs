# GetRealizedDataTransferCount

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the actual transfer count in bytes from the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
UInt64 (*GetRealizedDataTransferCount)(void *task);
```

## Return Value

Returns a UInt64 value of bytes transferred.

## Discussion

This method can be used to get the actual transfer count in bytes from the SCSITask.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575420-getrealizeddatatransfercount)*