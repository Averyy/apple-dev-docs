# ModeSense10

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Issues a MODE_SENSE_10 command to the device as defined in SPC-2.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ModeSense10)(void *self, SCSICmdField1Bit LLBAA, SCSICmdField1Bit DBD, SCSICmdField2Bit PC, SCSICmdField6Bit PAGE_CODE, void *buffer, SCSICmdField2Byte bufferSize, SCSITaskStatus *taskStatus, SCSI_Sense_Data *senseDataBuffer);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnNoMemory if a SCSITask couldn't be created, or kIOReturnExclusiveAccess if the device is already opened for exclusive access by another client.

#### Discussion

Once an MMCDeviceInterface is opened, the client may send this command to get mode page information from the device.

## Parameters

- `self`: Pointer to an MMCDeviceInterface for one IOService.
- `LLBAA`: The LLBAA bit as defined in SPC-2 for the MODE_SENSE_10 command.
- `DBD`: The DBD bit as defined in SPC-2 for the MODE_SENSE_10 command.
- `PC`: The PC bits as defined in SPC-2 for the MODE_SENSE_10 command.
- `PAGE_CODE`: The PAGE_CODE bits as defined in SPC-2 for the MODE_SENSE_10 command.
- `buffer`: Pointer to the buffer where the mode sense data should be placed.
- `bufferSize`: Size of the buffer.
- `taskStatus`: Pointer to a SCSITaskStatus to get the status of the SCSITask which was executed. Valid SCSITaskStatus values are defined in SCSITask.h
- `senseDataBuffer`: Pointer to a buffer the size of the SCSI_Sense_Data struct found in SCSICmds_REQUEST_SENSE_Defs.h. The sense data is only valid if the SCSITaskStatus is kSCSITaskStatus_CHECK_CONDITION.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/mmcdeviceinterface/1575392-modesense10)*