# USDPrim.Attribute

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
struct Attribute
```

## Topics

### Protocols
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
  A value that can be stored on an attribute in a Universal Scene Description file.
### Structures
- [USDPrim.Attribute.Spec](usdprim/attribute/spec.md)
  A handle to an attribute definition stored in a layer.
- [USDPrim.Attribute.ValueType](usdprim/attribute/valuetype.md)
  A type that describes the kind of value an attribute can store, such as `float3` or `token[]`.
### Initializers
- [init()](usdprim/attribute/init.md)
  An invalid attribute handle.
- [init?(USDStage.Object)](usdprim/attribute/init(_:)-8gu7p.md)
  Casts an object handle to an attribute handle.
- [init?(USDPrim.Property)](usdprim/attribute/init(_:)-8mm8c.md)
  Casts a property handle to an attribute handle.
### Instance Properties
- [var connections: [USDLayer.Path]](usdprim/attribute/connections.md)
  The connection target paths authored on this attribute.
- [var isValid: Bool](usdprim/attribute/isvalid.md)
  A Boolean value indicating whether this attribute is valid.
- [var name: USDToken](usdprim/attribute/name.md)
  The name of this attribute.
- [var path: USDLayer.Path](usdprim/attribute/path.md)
  The complete scene path to this attribute, relative to its stage.
- [var prim: USDPrim](usdprim/attribute/prim.md)
  The nearest prim that contains this attribute.
- [var primPath: USDLayer.Path](usdprim/attribute/primpath.md)
  The complete path to the nearest prim that contains this attribute.
- [var roleName: USDToken](usdprim/attribute/rolename.md)
  The name of this attribute type’s role, which clarifies the semantic purpose of its values.
- [var stage: USDStage](usdprim/attribute/stage.md)
  The stage that owns this attribute.
- [var timeSamples: [USDStage.TimeCode]](usdprim/attribute/timesamples.md)
  The composed set of time codes for which this attribute has authored time samples.
- [var typeName: USDPrim.Attribute.ValueType](usdprim/attribute/typename.md)
  The type of the values this attribute stores.
- [var variability: USDPrim.Property.Variability](usdprim/attribute/variability.md)
  The variability of this attribute, which indicates whether its value can change over time.
### Instance Methods
- [func clear() -> Bool](usdprim/attribute/clear.md)
  Clears the authored value of this attribute.
- [func setValue<T>(T, at: USDStage.TimeCode) -> Bool](usdprim/attribute/setvalue(_:at:).md)
  Sets this attribute’s value at the given time.
- [func value<T>(at: USDStage.TimeCode) -> T?](usdprim/attribute/value(at:).md)
  Returns this attribute’s value at the given time, or `nil` if unauthored.
### Default Implementations
- [CustomStringConvertible Implementations](usdprim/attribute/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [USDStage.Object.MetadataCollection](usdstage/object/metadatacollection.md)

## See Also

- [var attributes: [USDPrim.Attribute]](usdprim/attributes.md)
  The attributes of this prim, including those provided by its schemas.
- [var authoredAttributes: [USDPrim.Attribute]](usdprim/authoredattributes.md)
  The attributes of this prim that have an authored opinion.
- [func attribute(named: USDToken) -> USDPrim.Attribute](usdprim/attribute(named:).md)
  Returns the attribute with a given name on this prim.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdprim/attribute(at:).md)
  Returns the attribute at a given path, relative to this prim.
- [func hasAttribute(named: USDToken) -> Bool](usdprim/hasattribute(named:).md)
  Returns true if an attribute with a given name exists on this prim.
- [func makeAttribute(named: USDToken, as: USDPrim.Attribute.ValueType, custom: Bool, variability: USDPrim.Property.Variability) -> USDPrim.Attribute](usdprim/makeattribute(named:as:custom:variability:).md)
  Creates an attribute with the given name on this prim, or returns the existing attribute if one already exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute)*