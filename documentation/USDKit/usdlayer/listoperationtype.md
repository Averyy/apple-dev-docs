# USDLayer.ListOperationType

**Framework**: USDKit  
**Kind**: enum

Identifies an operation slot in a [`USDLayer.ListOperation`](usdlayer/listoperation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ListOperationType
```

## Topics

### Enumeration Cases
- [USDLayer.ListOperationType.appended](usdlayer/listoperationtype/appended.md)
  Items added to the back.
- [USDLayer.ListOperationType.deleted](usdlayer/listoperationtype/deleted.md)
  Items to remove during composition.
- [USDLayer.ListOperationType.explicit](usdlayer/listoperationtype/explicit.md)
  Items that replace the entire list.
- [USDLayer.ListOperationType.prepended](usdlayer/listoperationtype/prepended.md)
  Items added to the front.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](usdlayer/copy(from:to:in:).md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperation](usdlayer/listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [typealias Relocate](usdlayer/relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](usdlayer/relocatesmap.md)
  A mapping from source paths to target paths for relocations.
- [USDLayer.ChangeList](usdlayer/changelist.md)
  A list of changes made to a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/listoperationtype)*