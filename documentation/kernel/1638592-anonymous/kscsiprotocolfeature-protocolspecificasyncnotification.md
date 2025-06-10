# kSCSIProtocolFeature_ProtocolSpecificAsyncNotification

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolFeature_ProtocolSpecificAsyncNotification = 14
```

#### Discussion

Used to determine if the SCSI Protocol Services Driver supports asynchronous notifications from the drive. This is used to prevent polling for media, specifically for SATAPI devices on AHCI buses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_protocolspecificasyncnotification)*