# kSCSITaskStatus_TaskTimeoutOccurred

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.3+

## Declaration

```swift
kSCSITaskStatus_TaskTimeoutOccurred = 0x01
```

#### Discussion

If a task is aborted by the SCSI Protocol Layer due to it exceeding the timeout value specified by the task, the task status shall be set to kSCSITaskStatus_TaskTimeoutOccurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsitaskstatus/kscsitaskstatus_tasktimeoutoccurred)*