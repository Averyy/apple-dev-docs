# USDLayer.ChangeList.Entry

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A single change entry describing modifications at a path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Entry
```

## Topics

### Structures
- [USDLayer.ChangeList.Entry.Flags](./entry/flags-swift.struct.md)
  Boolean flags describing structural changes to a spec.
- [USDLayer.ChangeList.Entry.InfoChange](./entry/infochange.md)
  Old and new values for a changed info field.
### Instance Properties
- [var flags: USDLayer.ChangeList.Entry.Flags](./entry/flags-swift.property.md)
  Structural change flags for this entry.
- [var infoChanged: [(USDToken, USDLayer.ChangeList.Entry.InfoChange)]](./entry/infochanged.md)
  Info field changes, keyed by field name. Each `InfoChange` contains the old and new values.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/changelist/entry)*