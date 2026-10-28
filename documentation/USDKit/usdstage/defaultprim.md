# defaultPrim

**Framework**: USDKit  
**Kind**: property  
**Role**: Instance Property

The prim designated as this stage’s default entry point when the stage is referenced.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var defaultPrim: USDPrim? { get nonmutating set }
```

## Discussion

> **Note**: This property can be `nil` even if [`hasDefaultPrim`](./hasdefaultprim.md) is true. This indicates that there is an authored reference to a default prim, but it is invalid.

## See Also

### Accessing prims and properties
- [func prim(at: USDLayer.Path) -> USDPrim](./prim%28at%29.md)
  Returns the prim at a given path, if it exists.
- [func object(at: USDLayer.Path) -> USDStage.Object](./object%28at%29.md)
  Returns the object at a given path, if it exists.
- [func property(at: USDLayer.Path) -> USDPrim.Property](./property%28at%29.md)
  Returns the property at a given path, if it exists.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](./attribute%28at%29.md)
  Returns the attribute at a given path, if it exists.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](./relationship%28at%29.md)
  Returns the relationship at a given path, if it exists.
- [var pseudoRoot: USDPrim](./pseudoroot.md)
  The prim at the top of the stage’s namespace, whose path is `/`.
- [var hasDefaultPrim: Bool](./hasdefaultprim.md)
  Return true if this stage’s root layer has an authored opinion for the default prim layer metadata.
- [USDStage.Object](./object.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/defaultprim)*