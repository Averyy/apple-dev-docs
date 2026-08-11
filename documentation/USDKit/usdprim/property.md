# USDPrim.Property

**Framework**: USDKit  
**Kind**: struct

A named property on a prim, which is either an attribute or a relationship.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Property
```

## Topics

### Structures
- [USDPrim.Property.Spec](usdprim/property/spec.md)
  A handle to a property definition (attribute or relationship) stored in a layer.
### Initializers
- [init()](usdprim/property/init.md)
  An invalid property handle.
- [init?(USDStage.Object)](usdprim/property/init(_:)-2927p.md)
  Casts an object handle to a property handle.
- [init(USDPrim.Attribute)](usdprim/property/init(_:)-7co8b.md)
  Casts an attribute handle to a property handle.
- [init(USDPrim.Relationship)](usdprim/property/init(_:)-po4e.md)
### Instance Properties
- [var baseName: USDToken](usdprim/property/basename.md)
  The name of this property without its namespace prefix.
- [var isAuthored: Bool](usdprim/property/isauthored.md)
  A Boolean value that indicates whether this property has any authored opinions.
- [var isCustom: Bool](usdprim/property/iscustom.md)
  A Boolean value that indicates whether this property is a custom property not defined by a schema.
- [var isDefined: Bool](usdprim/property/isdefined.md)
  A Boolean value that indicates whether this property has a defining specification on the stage.
- [var isValid: Bool](usdprim/property/isvalid.md)
  A Boolean value indicating whether this property is valid.
- [var name: USDToken](usdprim/property/name.md)
  The name of this property.
- [var namespace: USDToken](usdprim/property/namespace.md)
  The namespace prefix of this property’s name, or an empty token if it has none.
- [var path: USDLayer.Path](usdprim/property/path.md)
  The complete scene path to this property, relative to its stage.
- [var prim: USDPrim](usdprim/property/prim.md)
  The nearest prim that contains this property.
- [var primPath: USDLayer.Path](usdprim/property/primpath.md)
  The complete path to the nearest prim that contains this property.
- [var stage: USDStage](usdprim/property/stage.md)
  The stage that owns this property.
### Enumerations
- [USDPrim.Property.Variability](usdprim/property/variability.md)
  Whether a property’s value can change over time.
### Default Implementations
- [CustomStringConvertible Implementations](usdprim/property/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [USDStage.Object.MetadataCollection](usdstage/object/metadatacollection.md)

## See Also

- [var properties: [USDPrim.Property]](usdprim/properties.md)
  The properties of this prim, including those provided by its schemas.
- [var authoredProperties: [USDPrim.Property]](usdprim/authoredproperties.md)
  The properties of this prim that have an authored opinion.
- [var propertyNames: [USDToken]](usdprim/propertynames.md)
  The names of this prim’s properties, including those provided by its schemas.
- [var authoredPropertyNames: [USDToken]](usdprim/authoredpropertynames.md)
  The names of this prim’s properties that have an authored opinion.
- [func property(named: USDToken) -> USDPrim.Property](usdprim/property(named:).md)
  Returns the property with a given name on this prim.
- [func hasProperty(named: USDToken) -> Bool](usdprim/hasproperty(named:).md)
  Returns true if an attribute or relationship with a given name exists.
- [func object(at: USDLayer.Path) -> USDStage.Object](usdprim/object(at:).md)
  Returns the object at a given path, relative to this prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property)*