# USDPrim.Relationship

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A property that connects a prim to one or more other objects in the stage by their paths.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Relationship
```

## Topics

### Structures
- [USDPrim.Relationship.Spec](./relationship/spec.md)
  A handle to a relationship definition stored in a layer.
### Initializers
- [init()](./relationship/init%28%29.md)
  An invalid relationship handle.
- [init?(USDPrim.Property)](./relationship/init%28_%29-8v165.md)
  Casts a property handle to a relationship handle.
- [init?(USDStage.Object)](./relationship/init%28_%29-sp7s.md)
  Casts an object handle to a relationship handle.
### Instance Properties
- [var isValid: Bool](./relationship/isvalid.md)
  A Boolean value indicating whether this relationship is valid.
- [var name: USDToken](./relationship/name.md)
  The name of this relationship.
- [var path: USDLayer.Path](./relationship/path.md)
  The complete scene path to this relationship, relative to its stage.
- [var prim: USDPrim](./relationship/prim.md)
  The nearest prim that contains this relationship.
- [var primPath: USDLayer.Path](./relationship/primpath.md)
  The complete path to the nearest prim that contains this relationship.
- [var stage: USDStage](./relationship/stage.md)
  The stage that owns this relationship.
- [var targets: [USDLayer.Path]](./relationship/targets.md)
  The target paths authored on this relationship.
### Default Implementations
- [CustomStringConvertible Implementations](./relationship/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [USDStage.Object.MetadataCollection](../usdstage/object/metadatacollection.md)

## See Also

### Accessing relationships
- [func relationship(named: USDToken) -> USDPrim.Relationship](./relationship%28named%29.md)
  Returns the relationship with a given name on this prim.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](./relationship%28at%29.md)
  Returns the relationship at a given path, relative to this prim.
- [func hasRelationship(named: USDToken) -> Bool](./hasrelationship%28named%29.md)
  Returns true if a relationship with a given name exists on this prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship)*