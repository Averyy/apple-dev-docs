# USDLayer.ListOperationType

**Framework**: USDKit  
**Kind**: enum  
**Role**: Enumeration

Identifies an operation slot in a [`USDLayer.ListOperation`](./listoperation.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum ListOperationType
```

## Topics

### Enumeration Cases
- [USDLayer.ListOperationType.appended](./listoperationtype/appended.md)
  Items added to the back.
- [USDLayer.ListOperationType.deleted](./listoperationtype/deleted.md)
  Items to remove during composition.
- [USDLayer.ListOperationType.explicit](./listoperationtype/explicit.md)
  Items that replace the entire list.
- [USDLayer.ListOperationType.prepended](./listoperationtype/prepended.md)
  Items added to the front.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Editing scene description
- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](./copy%28from,to,in%29.md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperation](./listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [typealias Relocate](./relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](./relocatesmap.md)
  A mapping from source paths to target paths for relocations.
- [USDLayer.ChangeList](./changelist.md)
  A list of changes made to a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/listoperationtype)*