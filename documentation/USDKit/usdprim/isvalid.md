# isValid

**Framework**: USDKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether this prim is valid.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var isValid: Bool { get }
```

## Discussion

A prim’s validity is connected to a [`USDStage`](../usdstage.md). A prim becomes invalid when the lifetime of its stage ends.

A prim will also expire if its stage no longer defines that prim. `isValid` is false if this prim has expired.

## See Also

### Identifying the prim
- [var path: USDLayer.Path](./path.md)
  The complete scene path to this prim, relative to its stage.
- [var primPath: USDLayer.Path](./primpath.md)
  The complete scene path to this prim, relative to its stage.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/isvalid)*