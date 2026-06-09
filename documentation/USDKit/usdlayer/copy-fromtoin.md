# copy(from:to:in:)

**Framework**: USDKit  
**Kind**: method

Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func copy(from srcPath: USDLayer.Path, to dstPath: USDLayer.Path, in dstLayer: USDLayer? = nil) -> Bool
```

#### Return Value

`true` on success.

## Parameters

- `srcPath`: The path of the source spec to copy.
- `dstPath`: The destination path.
- `dstLayer`: The destination layer. Pass `nil` to copy within this layer.

## See Also

- [USDLayer.ListOperation](usdlayer/listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [USDLayer.ListOperationType](usdlayer/listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](usdlayer/listoperation.md).
- [typealias Relocate](usdlayer/relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](usdlayer/relocatesmap.md)
  A mapping from source paths to target paths for relocations.
- [USDLayer.ChangeList](usdlayer/changelist.md)
  A list of changes made to a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/copy(from:to:in:))*