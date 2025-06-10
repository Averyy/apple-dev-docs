# kSCSIProtocolFeature_ProtocolAlwaysReportsAutosenseData

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolFeature_ProtocolAlwaysReportsAutosenseData = 11
```

#### Discussion

If the SCSI Protocol Services Driver always reports available autosense data when a kSCSITaskStatus_CHECK_CONDITION is set, then the protocol layer should return true. E.g. FireWire transport drivers should respond true to this.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_protocolalwaysreportsautosensedata)*