# kSCSIProtocolFeature_HierarchicalLogicalUnits

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolFeature_HierarchicalLogicalUnits = 15
```

#### Discussion

kSCSIProtocolFeature_HierarchicalLogicalUnits: If the SCSI Protocol Services layer supports hierarchical logical units, then the protocol services layer should report true and use IOSCSIProtocolServices::GetLogicalUnitBytes() to retrieve the full 8 bytes of LUN information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_hierarchicallogicalunits)*