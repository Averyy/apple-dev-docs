# USDLayer.RelocatesMap

**Framework**: USDKit  
**Kind**: typealias

A mapping from source paths to target paths for relocations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
typealias RelocatesMap = Dictionary<USDLayer.Path, USDLayer.Path>
```

## See Also

- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](usdlayer/copy(from:to:in:).md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperation](usdlayer/listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [USDLayer.ListOperationType](usdlayer/listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](usdlayer/listoperation.md).
- [typealias Relocate](usdlayer/relocate.md)
  A single path relocation from source to target.
- [USDLayer.ChangeList](usdlayer/changelist.md)
  A list of changes made to a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/relocatesmap)*