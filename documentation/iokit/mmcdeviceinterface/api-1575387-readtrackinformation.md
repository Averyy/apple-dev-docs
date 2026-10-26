# ReadTrackInformation

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Issues a READ_TRACK_INFORMATION command to the device as defined in MMC-2.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ReadTrackInformation)(void *self, SCSICmdField2Bit ADDRESS_NUMBER_TYPE, SCSICmdField4Byte LOGICAL_BLOCK_ADDRESS_TRACK_SESSION_NUMBER, void *buffer, SCSICmdField2Byte bufferSize, SCSITaskStatus *taskStatus, SCSI_Sense_Data *senseDataBuffer);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnNoMemory if a SCSITask couldn't be created, or kIOReturnExclusiveAccess if the device is already opened for exclusive access by another client.

#### Discussion

Once an MMCDeviceInterface is opened the client may send this command to read information about selected tracks on the disc.

## Parameters

- `self`: Pointer to an MMCDeviceInterface for one IOService.
- `ADDRESS_NUMBER_TYPE`: The ADDRESS/NUMBER_TYPE field as defined in MMC-2.
- `LOGICAL_BLOCK_ADDRESS_TRACK_SESSION_NUMBER`: The LOGICAL_BLOCK_ADDRESS/SESSION_NUMBER field as defined in MMC-2.
- `buffer`: Pointer to the buffer to be used for this function.
- `bufferSize`: The size of the data transfer requested.
- `taskStatus`: Pointer to a SCSITaskStatus to get the status of the SCSITask which was executed. Valid SCSITaskStatus values are defined in SCSITask.h
- `senseDataBuffer`: Pointer to a buffer the size of the SCSI_Sense_Data struct found in SCSICmds_REQUEST_SENSE_Defs.h. The sense data is only valid if the SCSITaskStatus is kSCSITaskStatus_CHECK_CONDITION.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/mmcdeviceinterface/1575387-readtrackinformation)*