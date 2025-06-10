# kSCSIProtocolFeature_MultiPathing

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolFeature_MultiPathing = 16
```

#### Discussion

kSCSIProtocolFeature_MultiPathing: If the SCSI Protocol Services layer supports multi-pathing, then the protocol services layer should report true. This is used to support multiple paths to a logical unit by creating a IOSCSIMultipathedLogicalUnit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_multipathing)*