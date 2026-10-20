# USDLayer.Relocate

**Framework**: USDKit  
**Kind**: typealias  
**Role**: Type Alias

A single path relocation from source to target.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
typealias Relocate = (source: USDLayer.Path, target: USDLayer.Path)
```

## See Also

### Editing scene description
- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](./copy%28from,to,in%29.md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperation](./listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [USDLayer.ListOperationType](./listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](./listoperation.md).
- [typealias RelocatesMap](./relocatesmap.md)
  A mapping from source paths to target paths for relocations.
- [USDLayer.ChangeList](./changelist.md)
  A list of changes made to a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/relocate)*