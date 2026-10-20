# USDStage.Object

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Object
```

## Topics

### Protocols
- [USDStage.Object.MetadataCollection](./object/metadatacollection.md)
  A scene graph object that possesses metadata.
- [USDStage.Object.MetadataValue](./object/metadatavalue.md)
  A value that can be stored as metadata in a Universal Scene Description file.
### Initializers
- [init()](./object/init%28%29.md)
  An invalid object handle.
- [init(USDPrim)](./object/init%28_%29-421oz.md)
- [init(USDPrim.Attribute)](./object/init%28_%29-44tvz.md)
  Casts an attribute handle to an object handle.
- [init(USDPrim.Relationship)](./object/init%28_%29-64kbz.md)
- [init(USDPrim.Property)](./object/init%28_%29-9xizj.md)
  Casts a property handle to an object handle.
### Instance Properties
- [var isValid: Bool](./object/isvalid.md)
  A Boolean value indicating whether this object is valid.
- [var name: USDToken](./object/name.md)
  The name of this scene graph object.
- [var path: USDLayer.Path](./object/path.md)
  The complete scene path to this object, relative to its stage.
- [var prim: USDPrim](./object/prim.md)
  The nearest prim that contains this object.
- [var primPath: USDLayer.Path](./object/primpath.md)
  The complete path to this prim, or to the nearest prim that contains this object.
- [var stage: USDStage](./object/stage.md)
  The stage that owns this object.
### Default Implementations
- [CustomStringConvertible Implementations](./object/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [USDStage.Object.MetadataCollection](./object/metadatacollection.md)

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
- [var defaultPrim: USDPrim?](./defaultprim.md)
  The prim designated as this stage’s default entry point when the stage is referenced.
- [var hasDefaultPrim: Bool](./hasdefaultprim.md)
  Return true if this stage’s root layer has an authored opinion for the default prim layer metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object)*