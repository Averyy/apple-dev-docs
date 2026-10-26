# ExecuteTaskSync

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to execute the SCSITask synchronously.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ExecuteTaskSync)(void *task, SCSI_Sense_Data *senseDataBuffer, SCSITaskStatus *outStatus, UInt64 *realizedTransferCount);
```

#### Return Value

Returns a valid IOReturn code such as kIOReturnSuccess, kIOReturnError, kIOReturnVMError, kIOReturnCannotWire, etc. NOTE: IOReturn is defined as kern_return_t and as such, you may get errors back that do not fall under the IOKit subsystem error domain (sys_iokit) defined in IOReturn.h.

#### Discussion

This method can be used to execute the SCSITask synchronously.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `senseDataBuffer`: Pointer to a buffer for REQUEST_SENSE data. May be NULL if caller does not wish to have sense data returned. If caller has previously called SetAutoSenseDataBuffer(), this parameter is ignored.
- `outStatus`: Pointer to an SCSITaskStatus. May be NULL if caller does not wish to have task status returned.
- `realizedTransferCount`: Pointer to an UInt64 which reflects how much data was actually transferred. May be NULL if caller does not wish to know how many bytes were transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575417-executetasksync)*