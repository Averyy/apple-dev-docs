# Inquiry

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Issues an INQUIRY command to the device as defined in SPC-2.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*Inquiry)(void *self, SCSICmd_INQUIRY_StandardData *inquiryBuffer, UInt32 inqBufferSize, SCSITaskStatus *taskStatus, SCSI_Sense_Data *senseDataBuffer);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnNoMemory if a SCSITask couldn't be created, or kIOReturnExclusiveAccess if the device is already opened for exclusive access by another client.

## Discussion

Once an MMCDeviceInterface is opened, the client may send this command to get inquiry data from the drive.

## Parameters

- `self`: Pointer to an MMCDeviceInterface for one IOService.
- `inquiryBuffer`: A pointer to a buffer the size of the SCSICmd_INQUIRY_StandardData struct found in SCSICmds_INQUIRY_Definitions.h.
- `inqBufferSize`: The amount of INQUIRY data to ask the device for (some devices return less INQUIRY data than the size of SCSICmd_INQUIRY_StandardData and will need to be reset if more than that amount is specified). This value must be less than the size of SCSICmd_INQUIRY_StandardData.
- `taskStatus`: Pointer to a SCSITaskStatus to get the status of the SCSITask which was executed. Valid SCSITaskStatus values are defined in SCSITask.h
- `senseDataBuffer`: Pointer to a buffer the size of the SCSI_Sense_Data struct found in SCSICmds_REQUEST_SENSE_Defs.h. The sense data is only valid if the SCSITaskStatus is kSCSITaskStatus_CHECK_CONDITION.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/mmcdeviceinterface/1575408-inquiry)*