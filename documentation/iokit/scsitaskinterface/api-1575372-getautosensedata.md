# GetAutoSenseData

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the auto-sense data from the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*GetAutoSenseData)(void *task, SCSI_Sense_Data *senseDataBuffer);
```

## Return Value

Returns kIOReturnSuccess if sense data is valid, otherwise kIOReturnError.

## Discussion

This method can be used to get the auto-sense data from the SCSITask.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `senseDataBuffer`: Pointer to a buffer the size of the SCSI_Sense_Data structure. If caller has previously called SetAutoSenseDataBuffer(), this routine will return an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575372-getautosensedata)*