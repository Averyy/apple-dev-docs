# kSCSIProtocolFeature_MaximumReadBlockTransferCount

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolFeature_MaximumReadBlockTransferCount = 6
```

#### Discussion

If the SCSI Protocol Services Driver has a maximum number of blocks that can be transfered in a read request, it will return true to this query and return the block count in the UInt32 pointer that is passed in as the serviceValue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_maximumreadblocktransfercount)*