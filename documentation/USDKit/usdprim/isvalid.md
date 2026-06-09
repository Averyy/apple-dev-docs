# isValid

**Framework**: USDKit  
**Kind**: property

A Boolean value indicating whether this prim is valid.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

A prim’s validity is connected to a [`USDStage`](usdstage-4sfi1.md). A prim becomes invalid when the lifetime of its stage ends.

A prim will also expire if its stage no longer defines that prim. `isValid` is false if this prim has expired.

## See Also

- [var path: USDLayer.Path](usdprim/path.md)
  The complete scene path to this prim, relative to its stage.
- [var primPath: USDLayer.Path](usdprim/primpath.md)
  The complete scene path to this prim, relative to its stage.
- [var specifier: USDPrim.Specifier](usdprim/specifier-swift.property.md)
- [var stage: USDStage](usdprim/stage.md)
  The stage that owns this prim.
- [var parent: USDPrim?](usdprim/parent.md)
  The immediate parent prim of this prim.
- [var description: String](usdprim/description.md)
  A summary description of this prim.
- [USDPrim.Specifier](usdprim/specifier-swift.enum.md)
  How a prim definition behaves in composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/isvalid)*