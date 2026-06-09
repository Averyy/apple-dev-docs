# USDStage.Object

**Framework**: USDKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Object
```

## Topics

### Protocols
- [USDStage.Object.MetadataCollection](usdstage-4sfi1/object/metadatacollection.md)
  A scene graph object that possesses metadata.
### Initializers
- [init()](usdstage-4sfi1/object/init.md)
  An invalid object handle.
- [init(USDPrim)](usdstage-4sfi1/object/init(_:)-421oz.md)
- [init(USDPrim.Attribute)](usdstage-4sfi1/object/init(_:)-44tvz.md)
  Casts an attribute handle to an object handle.
- [init(USDPrim.Relationship)](usdstage-4sfi1/object/init(_:)-64kbz.md)
- [init(USDPrim.Property)](usdstage-4sfi1/object/init(_:)-9xizj.md)
  Casts a property handle to an object handle.
### Instance Properties
- [var isValid: Bool](usdstage-4sfi1/object/isvalid.md)
  A Boolean value indicating whether this object is valid.
- [var name: USDToken](usdstage-4sfi1/object/name.md)
  The name of this object.
- [var path: USDLayer.Path](usdstage-4sfi1/object/path.md)
  The complete scene path to this object, relative to its stage.
- [var prim: USDPrim](usdstage-4sfi1/object/prim.md)
  The nearest prim that contains this object.
- [var primPath: USDLayer.Path](usdstage-4sfi1/object/primpath.md)
  The complete path to this prim, or to the nearest prim that contains this object.
- [var stage: USDStage](usdstage-4sfi1/object/stage.md)
  The stage that owns this object.
### Default Implementations
- [CustomStringConvertible Implementations](usdstage-4sfi1/object/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [USDStage.Object.MetadataCollection](usdstage-4sfi1/object/metadatacollection.md)

## See Also

- [func prim(at: USDLayer.Path) -> USDPrim](usdstage-4sfi1/prim(at:).md)
- [func object(at: USDLayer.Path) -> USDStage.Object](usdstage-4sfi1/object(at:).md)
- [func property(at: USDLayer.Path) -> USDPrim.Property](usdstage-4sfi1/property(at:).md)
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdstage-4sfi1/attribute(at:).md)
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](usdstage-4sfi1/relationship(at:).md)
- [var pseudoRoot: USDPrim](usdstage-4sfi1/pseudoroot.md)
- [var defaultPrim: USDPrim?](usdstage-4sfi1/defaultprim.md)
- [var hasDefaultPrim: Bool](usdstage-4sfi1/hasdefaultprim.md)
  Return true if this stage’s root layer has an authored opinion for the default prim layer metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/object)*