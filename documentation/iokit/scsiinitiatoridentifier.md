# SCSIInitiatorIdentifier

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

64-bit number to represent a SCSI Initiator Device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
typedef SCSIDeviceIdentifier SCSIInitiatorIdentifier;
```

#### Discussion

If the identifier is for an initiator only and not a target, then SCSIInitiatorIdentifier should be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsiinitiatoridentifier)*