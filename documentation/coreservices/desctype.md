# DescType

**Framework**: Core Services  
**Kind**: tdef

Specifies the type of the data stored in an `AEDesc` descriptor.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias DescType = ResType
```

#### Discussion

A `DescType` data type is a four-character code that stores a value that identifies the data in an [`AEDesc`](aedesc.md) descriptor, the basic building block for all Apple events.

The descriptor type constants used by the Apple Event Manager are described in [`Descriptor Type Constants`](apple_events/1542788-descriptor_type_constants.md) and [`Key Form and Descriptor Type Object Specifier Constants`](apple_events/1572731-key_form_and_descriptor_type_obj.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/desctype)*