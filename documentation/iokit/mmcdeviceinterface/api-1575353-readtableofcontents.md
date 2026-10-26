# ReadTableOfContents

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Issues a READ_TOC_PMA_ATIP command to the device as defined in MMC-2/SFF-8020i.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ReadTableOfContents)(void *self, SCSICmdField1Bit MSF, SCSICmdField4Bit FORMAT, SCSICmdField1Byte TRACK_SESSION_NUMBER, void *buffer, SCSICmdField2Byte bufferSize, SCSITaskStatus *taskStatus, SCSI_Sense_Data *senseDataBuffer);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnNoMemory if a SCSITask couldn't be created, or kIOReturnExclusiveAccess if the device is already opened for exclusive access by another client.

#### Discussion

Once an MMCDeviceInterface is opened the client may send this command to read the table of contents from the media.

## Parameters

- `self`: Pointer to an MMCDeviceInterface for one IOService.
- `MSF`: The MSF bit as defined in MMC-2/SFF-8020i.
- `FORMAT`: The FORMAT field as defined in MMC-2/SFF-8020i.
- `TRACK_SESSION_NUMBER`: The TRACK_SESSION_NUMBER field as defined in MMC-2/SFF-8020i.
- `buffer`: Pointer to the buffer to be used for this function.
- `bufferSize`: The size of the data transfer requested.
- `taskStatus`: Pointer to a SCSITaskStatus to get the status of the SCSITask which was executed. Valid SCSITaskStatus values are defined in SCSITask.h
- `senseDataBuffer`: Pointer to a buffer the size of the SCSI_Sense_Data struct found in SCSICmds_REQUEST_SENSE_Defs.h. The sense data is only valid if the SCSITaskStatus is kSCSITaskStatus_CHECK_CONDITION.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/mmcdeviceinterface/1575353-readtableofcontents)*