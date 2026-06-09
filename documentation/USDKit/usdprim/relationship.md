# USDPrim.Relationship

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
struct Relationship
```

## Topics

### Structures
- [USDPrim.Relationship.Spec](usdprim/relationship/spec.md)
  A handle to a relationship definition stored in a layer.
### Initializers
- [init()](usdprim/relationship/init.md)
  An invalid relationship handle.
- [init?(USDPrim.Property)](usdprim/relationship/init(_:)-8v165.md)
  Casts a property handle to a relationship handle.
- [init?(USDStage.Object)](usdprim/relationship/init(_:)-sp7s.md)
  Casts an object handle to a relationship handle.
### Instance Properties
- [var isValid: Bool](usdprim/relationship/isvalid.md)
  A Boolean value indicating whether this relationship is valid.
- [var name: USDToken](usdprim/relationship/name.md)
  The name of this relationship.
- [var path: USDLayer.Path](usdprim/relationship/path.md)
  The complete scene path to this relationship, relative to its stage.
- [var prim: USDPrim](usdprim/relationship/prim.md)
  The nearest prim that contains this relationship.
- [var primPath: USDLayer.Path](usdprim/relationship/primpath.md)
  The complete path to the nearest prim that contains this relationship.
- [var stage: USDStage](usdprim/relationship/stage.md)
  The stage that owns this relationship.
### Default Implementations
- [CustomStringConvertible Implementations](usdprim/relationship/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [USDStage.Object.MetadataCollection](usdstage-4sfi1/object/metadatacollection.md)

## See Also

- [func relationship(named: USDToken) -> USDPrim.Relationship?](usdprim/relationship(named:).md)
  Returns the relationship with a given name on this prim.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](usdprim/relationship(at:).md)
  Returns the relationship at a given path, relative to this prim.
- [func hasRelationship(named: USDToken) -> Bool](usdprim/hasrelationship(named:).md)
  Returns true if a relationship with a given name exists on this prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship)*