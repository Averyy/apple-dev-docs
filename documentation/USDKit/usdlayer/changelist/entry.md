# USDLayer.ChangeList.Entry

**Framework**: USDKit  
**Kind**: struct

A single change entry describing modifications at a path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Entry
```

## Topics

### Structures
- [USDLayer.ChangeList.Entry.Flags](usdlayer/changelist/entry/flags-swift.struct.md)
  Boolean flags describing structural changes to a spec.
- [USDLayer.ChangeList.Entry.InfoChange](usdlayer/changelist/entry/infochange.md)
  Old and new values for a changed info field.
### Instance Properties
- [var flags: USDLayer.ChangeList.Entry.Flags](usdlayer/changelist/entry/flags-swift.property.md)
  Structural change flags for this entry.
- [var infoChanged: [(USDToken, USDLayer.ChangeList.Entry.InfoChange)]](usdlayer/changelist/entry/infochanged.md)
  Info field changes, keyed by field name. Each `InfoChange` contains the old and new values.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/changelist/entry)*