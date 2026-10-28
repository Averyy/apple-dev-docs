# kSCSITaskStatus_ProtocolTimeoutOccurred

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
kSCSITaskStatus_ProtocolTimeoutOccurred = 0x02
```

## Discussion

If a task is aborted by the SCSI Protocol Layer due to it exceeding a timeout value specified by the support for the protocol or a related specification, the task status shall be set to kSCSITaskStatus_ProtocolTimeoutOccurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskstatus/kscsitaskstatus_protocoltimeoutoccurred)*