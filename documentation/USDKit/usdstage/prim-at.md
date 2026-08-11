# prim(at:)

**Framework**: USDKit  
**Kind**: method

Returns the prim at a given path, if it exists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func prim(at path: USDLayer.Path) -> USDPrim
```

#### Discussion

If `path` resolves to a prim beneath an instance, returns an instance proxy prim if a prim exists at the corresponding path in that instance’s prototype.

If no prim exists at the resolved path, returns an invalid prim handle.

## See Also

- [func object(at: USDLayer.Path) -> USDStage.Object](usdstage/object(at:).md)
  Returns the object at a given path, if it exists.
- [func property(at: USDLayer.Path) -> USDPrim.Property](usdstage/property(at:).md)
  Returns the property at a given path, if it exists.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdstage/attribute(at:).md)
  Returns the attribute at a given path, if it exists.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](usdstage/relationship(at:).md)
  Returns the relationship at a given path, if it exists.
- [var pseudoRoot: USDPrim](usdstage/pseudoroot.md)
  The prim at the top of the stage’s namespace, whose path is `/`.
- [var defaultPrim: USDPrim?](usdstage/defaultprim.md)
  The prim designated as this stage’s default entry point when the stage is referenced.
- [var hasDefaultPrim: Bool](usdstage/hasdefaultprim.md)
  Return true if this stage’s root layer has an authored opinion for the default prim layer metadata.
- [USDStage.Object](usdstage/object.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/prim(at:))*