# USDPrim.Specifier

**Framework**: USDKit  
**Kind**: enum

How a prim definition behaves in composition.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Specifier
```

## Topics

### Enumeration Cases
- [USDPrim.Specifier.class](usdprim/specifier-swift.enum/class.md)
  Defines an abstract template for inheritance.
- [USDPrim.Specifier.def](usdprim/specifier-swift.enum/def.md)
  Creates a concrete prim.
- [USDPrim.Specifier.over](usdprim/specifier-swift.enum/over.md)
  Applies only if the prim exists in a weaker layer.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [var path: USDLayer.Path](usdprim/path.md)
  The complete scene path to this prim, relative to its stage.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/specifier-swift.enum)*