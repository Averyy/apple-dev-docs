# kSCSITaskStatus_TaskTimeoutOccurred

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
kSCSITaskStatus_TaskTimeoutOccurred = 0x01
```

#### Discussion

If a task is aborted by the SCSI Protocol Layer due to it exceeding the timeout value specified by the task, the task status shall be set to kSCSITaskStatus_TaskTimeoutOccurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskstatus/kscsitaskstatus_tasktimeoutoccurred)*