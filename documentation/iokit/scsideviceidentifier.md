# SCSIDeviceIdentifier

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

64-bit number to represent a SCSI Device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
typedef UInt64 SCSIDeviceIdentifier;
```

## Discussion

If the identifier can either be that of an initiator or a target, SCSIDeviceIdentifier should be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsideviceidentifier)*