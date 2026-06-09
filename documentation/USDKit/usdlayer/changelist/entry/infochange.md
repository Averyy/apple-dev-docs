# USDLayer.ChangeList.Entry.InfoChange

**Framework**: USDKit  
**Kind**: struct

Old and new values for a changed info field.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct InfoChange
```

## Topics

### Instance Properties
- [var newValue: USDValue?](usdlayer/changelist/entry/infochange/newvalue.md)
  The value after the change, or `nil` if the field was removed.
- [var oldValue: USDValue?](usdlayer/changelist/entry/infochange/oldvalue.md)
  The value before the change, or `nil` if the field was added.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/changelist/entry/infochange)*