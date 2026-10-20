# USDPrim.Specifier

**Framework**: USDKit  
**Kind**: enum  
**Role**: Enumeration

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
- [USDPrim.Specifier.class](./specifier-swift.enum/class.md)
  Defines an abstract template for inheritance.
- [USDPrim.Specifier.def](./specifier-swift.enum/def.md)
  Creates a concrete prim.
- [USDPrim.Specifier.over](./specifier-swift.enum/over.md)
  Applies only if the prim exists in a weaker layer.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDValueProtocol](../usdvalueprotocol.md)

## See Also

### Identifying the prim
- [var path: USDLayer.Path](./path.md)
  The complete scene path to this prim, relative to its stage.
- [var primPath: USDLayer.Path](./primpath.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/specifier-swift.enum)*