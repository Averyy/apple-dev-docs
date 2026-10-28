# copy(from:to:in:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@discardableResult
func copy(from srcPath: USDLayer.Path, to dstPath: USDLayer.Path, in dstLayer: USDLayer? = nil) -> Bool
```

## Return Value

`true` on success.

## Parameters

- `srcPath`: The path of the source spec to copy.
- `dstPath`: The destination path.
- `dstLayer`: The destination layer. Pass `nil` to copy within this layer.

## See Also

### Editing scene description
- [USDLayer.ListOperation](./listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [USDLayer.ListOperationType](./listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](./listoperation.md).
- [typealias Relocate](./relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](./relocatesmap.md)
  A mapping from source paths to target paths for relocations.
- [USDLayer.ChangeList](./changelist.md)
  A list of changes made to a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/copy(from:to:in:))*