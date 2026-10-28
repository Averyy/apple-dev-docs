# SetWriteParametersModePage

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Issues a MODE_SELECT command to the device as defined in SPC-2 with the Write Parameters Mode Page Code as defined in MMC-2.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*SetWriteParametersModePage)(void *self, void *buffer, SCSICmdField1Byte bufferSize, SCSITaskStatus *taskStatus, SCSI_Sense_Data *senseDataBuffer);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnNoMemory if a SCSITask couldn't be created, or kIOReturnExclusiveAccess if the device is already opened for exclusive access by another client.

## Discussion

Once an MMCDeviceInterface is opened, the client may send this command to set the default values returned in a READ_DISC_INFORMATION call.

## Parameters

- `buffer`: Pointer to buffer (including mode parameter header).
- `taskStatus`: Pointer to a SCSITaskStatus to get the status of the SCSITask which was executed. Valid SCSITaskStatus values are defined in SCSITask.h
- `senseDataBuffer`: Pointer to a buffer the size of the SCSI_Sense_Data struct found in SCSICmds_REQUEST_SENSE_Defs.h. The sense data is only valid if the SCSITaskStatus is kSCSITaskStatus_CHECK_CONDITION.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/mmcdeviceinterface/1575346-setwriteparametersmodepage)*