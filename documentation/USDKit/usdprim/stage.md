# stage

**Framework**: USDKit  
**Kind**: property

The stage that owns this prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var stage: USDStage { get }
```

#### Discussion

A prim’s state and validity is connected to its stage. A prim becomes invalid when the lifetime of its stage ends. It can also become invalid when the stage is modified.

## See Also

- [var path: USDLayer.Path](usdprim/path.md)
  The complete scene path to this prim, relative to its stage.
- [var primPath: USDLayer.Path](usdprim/primpath.md)
  The complete scene path to this prim, relative to its stage.
- [var isValid: Bool](usdprim/isvalid.md)
  A Boolean value indicating whether this prim is valid.
- [var specifier: USDPrim.Specifier](usdprim/specifier-swift.property.md)
- [var parent: USDPrim?](usdprim/parent.md)
  The immediate parent prim of this prim.
- [var description: String](usdprim/description.md)
  A summary description of this prim.
- [USDPrim.Specifier](usdprim/specifier-swift.enum.md)
  How a prim definition behaves in composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/stage)*