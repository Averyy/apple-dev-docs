# USDLayer.ChangeList

**Framework**: USDKit  
**Kind**: struct

A list of changes made to a layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ChangeList
```

#### Overview

Used by the layer change notification system to describe what modifications occurred between two states of a layer.

## Topics

### Structures
- [USDLayer.ChangeList.Entry](usdlayer/changelist/entry.md)
  A single change entry describing modifications at a path.
### Instance Properties
- [var entries: [(USDLayer.Path, USDLayer.ChangeList.Entry)]](usdlayer/changelist/entries.md)
  All change entries, keyed by the path of the affected spec.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](usdlayer/copy(from:to:in:).md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperation](usdlayer/listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [USDLayer.ListOperationType](usdlayer/listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](usdlayer/listoperation.md).
- [typealias Relocate](usdlayer/relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](usdlayer/relocatesmap.md)
  A mapping from source paths to target paths for relocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/changelist)*