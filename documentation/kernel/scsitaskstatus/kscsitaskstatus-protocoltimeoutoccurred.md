# kSCSITaskStatus_ProtocolTimeoutOccurred

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.3+

## Declaration

```swift
kSCSITaskStatus_ProtocolTimeoutOccurred = 0x02
```

#### Discussion

If a task is aborted by the SCSI Protocol Layer due to it exceeding a timeout value specified by the support for the protocol or a related specification, the task status shall be set to kSCSITaskStatus_ProtocolTimeoutOccurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsitaskstatus/kscsitaskstatus_protocoltimeoutoccurred)*