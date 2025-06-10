# kSCSIProtocolFeature_MaximumWriteTransferByteCount

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolFeature_MaximumWriteTransferByteCount = 9
```

#### Discussion

If the SCSI Protocol Services Driver has a maximum byte count that can be transferred in a write request, it will return true to this query and return the byte count in the UInt64 pointer that is passed in as the serviceValue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_maximumwritetransferbytecount)*