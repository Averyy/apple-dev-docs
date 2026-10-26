# kSCSITaskStatus_ACA_ACTIVE

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kSCSITaskStatus_ACA_ACTIVE = 0x30
```

#### Discussion

The task completed with a status of ACA_ACTIVE. The device server may need the initiator to clear the Auto-Contingent Allegiance condition before it will respond to new commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskstatus/kscsitaskstatus_aca_active)*