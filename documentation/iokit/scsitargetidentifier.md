# SCSITargetIdentifier

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

64-bit number to represent a SCSI Target Device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
typedef SCSIDeviceIdentifier SCSITargetIdentifier;
```

## Discussion

If the identifier is for a target only and not an initiator, then SCSITargetIdentifier should be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitargetidentifier)*