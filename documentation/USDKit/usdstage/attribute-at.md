# attribute(at:)

**Framework**: USDKit  
**Kind**: method

Returns the attribute at a given path, if it exists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func attribute(at path: USDLayer.Path) -> USDPrim.Attribute
```

#### Discussion

If no attribute exists at the resolved path, returns an invalid attribute handle.

## See Also

- [func prim(at: USDLayer.Path) -> USDPrim](usdstage/prim(at:).md)
  Returns the prim at a given path, if it exists.
- [func object(at: USDLayer.Path) -> USDStage.Object](usdstage/object(at:).md)
  Returns the object at a given path, if it exists.
- [func property(at: USDLayer.Path) -> USDPrim.Property](usdstage/property(at:).md)
  Returns the property at a given path, if it exists.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/attribute(at:))*