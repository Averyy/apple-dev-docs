# USDLayer.ChangeList

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A list of changes made to a layer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ChangeList
```

#### Overview

Used by the layer change notification system to describe what modifications occurred between two states of a layer.

## Topics

### Structures
- [USDLayer.ChangeList.Entry](./changelist/entry.md)
  A single change entry describing modifications at a path.
### Instance Properties
- [var entries: [(USDLayer.Path, USDLayer.ChangeList.Entry)]](./changelist/entries.md)
  All change entries, keyed by the path of the affected spec.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Editing scene description
- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](./copy%28from,to,in%29.md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperation](./listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [USDLayer.ListOperationType](./listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](./listoperation.md).
- [typealias Relocate](./relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](./relocatesmap.md)
  A mapping from source paths to target paths for relocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/changelist)*