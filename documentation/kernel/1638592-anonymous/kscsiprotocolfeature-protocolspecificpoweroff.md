# kSCSIProtocolFeature_ProtocolSpecificPowerOff

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolFeature_ProtocolSpecificPowerOff = 12
```

#### Discussion

If the SCSI Protocol Services Driver supports removing the power to the drive, then the protocol layer should return true. This is used for aggressive power management, specifically for ATAPI devices on ATA buses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_protocolspecificpoweroff)*