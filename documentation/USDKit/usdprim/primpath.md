# primPath

**Framework**: USDKit  
**Kind**: property  
**Role**: Instance Property

The complete scene path to this prim, relative to its stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var primPath: USDLayer.Path { get }
```

## Discussion

This property is equivalent to [`path`](./path.md).

## See Also

### Identifying the prim
- [var path: USDLayer.Path](./path.md)
  The complete scene path to this prim, relative to its stage.
- [var isValid: Bool](./isvalid.md)
  A Boolean value indicating whether this prim is valid.
- [var specifier: USDPrim.Specifier](./specifier-swift.property.md)
  The specifier that describes how this prim is defined, such as `def`, `over`, or `class`.
- [var stage: USDStage](./stage.md)
  The stage that owns this prim.
- [var parent: USDPrim?](./parent.md)
  The immediate parent prim of this prim.
- [var description: String](./description.md)
  A summary description of this prim.
- [USDPrim.Specifier](./specifier-swift.enum.md)
  How a prim definition behaves in composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/primpath)*