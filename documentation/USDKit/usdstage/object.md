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
- [USDStage.Object.MetadataCollection](usdstage/object/metadatacollection.md)
  A scene graph object that possesses metadata.
- [USDStage.Object.MetadataValue](usdstage/object/metadatavalue.md)
  A value that can be stored as metadata in a Universal Scene Description file.
### Initializers
- [init()](usdstage/object/init.md)
  An invalid object handle.
- [init(USDPrim)](usdstage/object/init(_:)-421oz.md)
- [init(USDPrim.Attribute)](usdstage/object/init(_:)-44tvz.md)
  Casts an attribute handle to an object handle.
- [init(USDPrim.Relationship)](usdstage/object/init(_:)-64kbz.md)
- [init(USDPrim.Property)](usdstage/object/init(_:)-9xizj.md)
  Casts a property handle to an object handle.
### Instance Properties
- [var isValid: Bool](usdstage/object/isvalid.md)
  A Boolean value indicating whether this object is valid.
- [var name: USDToken](usdstage/object/name.md)
  The name of this scene graph object.
- [var path: USDLayer.Path](usdstage/object/path.md)
  The complete scene path to this object, relative to its stage.
- [var prim: USDPrim](usdstage/object/prim.md)
  The nearest prim that contains this object.
- [var primPath: USDLayer.Path](usdstage/object/primpath.md)
  The complete path to this prim, or to the nearest prim that contains this object.
- [var stage: USDStage](usdstage/object/stage.md)
  The stage that owns this object.
### Default Implementations
- [CustomStringConvertible Implementations](usdstage/object/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [USDStage.Object.MetadataCollection](usdstage/object/metadatacollection.md)

## See Also

- [func prim(at: USDLayer.Path) -> USDPrim](usdstage/prim(at:).md)
  Returns the prim at a given path, if it exists.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object)*