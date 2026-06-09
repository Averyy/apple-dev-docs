# description

**Framework**: USDKit  
**Kind**: property

A summary description of this prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var description: String { get }
```

#### Discussion

This property is safe to access on an invalid or expired prim.

## See Also

- [var path: USDLayer.Path](usdprim/path.md)
  The complete scene path to this prim, relative to its stage.
- [var primPath: USDLayer.Path](usdprim/primpath.md)
  The complete scene path to this prim, relative to its stage.
- [var isValid: Bool](usdprim/isvalid.md)
  A Boolean value indicating whether this prim is valid.
- [var specifier: USDPrim.Specifier](usdprim/specifier-swift.property.md)
- [var stage: USDStage](usdprim/stage.md)
  The stage that owns this prim.
- [var parent: USDPrim?](usdprim/parent.md)
  The immediate parent prim of this prim.
- [USDPrim.Specifier](usdprim/specifier-swift.enum.md)
  How a prim definition behaves in composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/description)*