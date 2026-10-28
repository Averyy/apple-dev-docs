# SetScatterGatherEntries

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to set the task's scatter-gather list entries.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*SetScatterGatherEntries)(void *task, SCSITaskSGElement *inScatterGatherList, UInt8 inScatterGatherEntries, UInt64 inTransferCount, UInt8 inTransferDirection);
```

## Return Value

Returns kIOReturnSucces or kIOReturnError.

## Discussion

This method can be used to set the SCSITask's scatter-gather list entries. Scatter-gather lists are represented as an array of SCSITaskSGElements. The SCSITaskSGElement structure has two elements, the address of the buffer and the length of the buffer.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `inScatterGatherList`: Pointer to an array of SCSITaskSGElements.
- `inScatterGatherEntries`: The size of the inScatterGatherList array.
- `inTransferCount`: The TOTAL amount of data to transfer. The length of all the entries in the scatter-gather list should at least add up to the amount in inTransferCount.
- `inTransferDirection`: The transfer direction as defined in SCSITask.h. Valid values are kSCSIDataTransfer_NoDataTransfer, kSCSIDataTransfer_FromTargetToInitiator, and kSCSIDataTransfer_FromInitiatorToTarget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575397-setscattergatherentries)*