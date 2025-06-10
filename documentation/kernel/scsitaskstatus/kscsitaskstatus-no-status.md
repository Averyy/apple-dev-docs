# kSCSITaskStatus_No_Status

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.0+

## Declaration

```swift
kSCSITaskStatus_No_Status = 0xFF
```

#### Discussion

This status is not defined by the SCSI specifications, but is here to provide a status that can be returned in cases where there is not status available from the device or protocol, for example, when the service response is neither TASK_COMPLETED nor LINK_COMMAND_COMPLETE or when the service response is SERVICE_DELIVERY_OR_TARGET_FAILURE and the reason for failure could not be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsitaskstatus/kscsitaskstatus_no_status)*