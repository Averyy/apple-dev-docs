# kSCSIProtocolNotification_VerifyDeviceState

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolNotification_VerifyDeviceState = 0x69000020
```

#### Discussion

Private message sent between a SCSI protocol service provider and SCSI application layer driver to indicate device state may have changed and the device state should be re-verified by the SCSI Application Layer driver. An example would be a bus reset which clears the tray locking state of an ATAPI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638595-anonymous/kscsiprotocolnotification_verifydevicestate)*