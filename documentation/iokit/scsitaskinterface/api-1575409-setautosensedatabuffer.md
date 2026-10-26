# SetAutoSenseDataBuffer

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to set the auto-sense data for the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*SetAutoSenseDataBuffer)(void *task, SCSI_Sense_Data *senseDataBuffer, UInt8 senseDataLength);
```

#### Return Value

Returns kIOReturnSuccess if sense data buffer was set, otherwise kIOReturnError.

#### Discussion

This method can be used to set the auto-sense data buffer for the SCSITask.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `senseDataBuffer`: Pointer to a buffer. May be be NULL if the caller wants to restrict the size to be less than the normal 18 bytes of sense data.
- `senseDataLength`: Amount of sense data to retrieve. Zero is not a valid value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575409-setautosensedatabuffer)*