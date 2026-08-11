# path

**Framework**: USDKit  
**Kind**: property

The complete scene path to this prim, relative to its stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var path: USDLayer.Path { get }
```

## See Also

- [var primPath: USDLayer.Path](usdprim/primpath.md)
  The complete scene path to this prim, relative to its stage.
- [var isValid: Bool](usdprim/isvalid.md)
  A Boolean value indicating whether this prim is valid.
- [var specifier: USDPrim.Specifier](usdprim/specifier-swift.property.md)
  The specifier that describes how this prim is defined, such as `def`, `over`, or `class`.
- [var stage: USDStage](usdprim/stage.md)
  The stage that owns this prim.
- [var parent: USDPrim?](usdprim/parent.md)
  The immediate parent prim of this prim.
- [var description: String](usdprim/description.md)
  A summary description of this prim.
- [USDPrim.Specifier](usdprim/specifier-swift.enum.md)
  How a prim definition behaves in composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/path)*