# USDPrim.Attribute

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
struct Attribute
```

## Topics

### Protocols
- [USDPrim.Attribute.Value](./attribute/value.md)
  A value that can be stored on an attribute in a Universal Scene Description file.
### Structures
- [USDPrim.Attribute.Spec](./attribute/spec.md)
  A handle to an attribute definition stored in a layer.
- [USDPrim.Attribute.ValueType](./attribute/valuetype.md)
  A type that describes the kind of value an attribute can store, such as `float3` or `token[]`.
### Initializers
- [init()](./attribute/init%28%29.md)
  An invalid attribute handle.
- [init?(USDStage.Object)](./attribute/init%28_%29-8gu7p.md)
  Casts an object handle to an attribute handle.
- [init?(USDPrim.Property)](./attribute/init%28_%29-8mm8c.md)
  Casts a property handle to an attribute handle.
### Instance Properties
- [var connections: [USDLayer.Path]](./attribute/connections.md)
  The connection target paths authored on this attribute.
- [var isValid: Bool](./attribute/isvalid.md)
  A Boolean value indicating whether this attribute is valid.
- [var name: USDToken](./attribute/name.md)
  The name of this attribute.
- [var path: USDLayer.Path](./attribute/path.md)
  The complete scene path to this attribute, relative to its stage.
- [var prim: USDPrim](./attribute/prim.md)
  The nearest prim that contains this attribute.
- [var primPath: USDLayer.Path](./attribute/primpath.md)
  The complete path to the nearest prim that contains this attribute.
- [var roleName: USDToken](./attribute/rolename.md)
  The name of this attribute type’s role, which clarifies the semantic purpose of its values.
- [var stage: USDStage](./attribute/stage.md)
  The stage that owns this attribute.
- [var timeSamples: [USDStage.TimeCode]](./attribute/timesamples.md)
  The composed set of time codes for which this attribute has authored time samples.
- [var typeName: USDPrim.Attribute.ValueType](./attribute/typename.md)
  The type of the values this attribute stores.
- [var variability: USDPrim.Property.Variability](./attribute/variability.md)
  The variability of this attribute, which indicates whether its value can change over time.
### Instance Methods
- [func clear() -> Bool](./attribute/clear%28%29.md)
  Clears the authored value of this attribute.
- [func setValue<T>(T, at: USDStage.TimeCode) -> Bool](./attribute/setvalue%28_,at%29.md)
  Sets this attribute’s value at the given time.
- [func value<T>(at: USDStage.TimeCode) -> T?](./attribute/value%28at%29.md)
  Returns this attribute’s value at the given time, or `nil` if unauthored.
### Default Implementations
- [CustomStringConvertible Implementations](./attribute/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [USDStage.Object.MetadataCollection](../usdstage/object/metadatacollection.md)

## See Also

### Accessing attributes
- [var attributes: [USDPrim.Attribute]](./attributes.md)
  The attributes of this prim, including those provided by its schemas.
- [var authoredAttributes: [USDPrim.Attribute]](./authoredattributes.md)
  The attributes of this prim that have an authored opinion.
- [func attribute(named: USDToken) -> USDPrim.Attribute](./attribute%28named%29.md)
  Returns the attribute with a given name on this prim.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](./attribute%28at%29.md)
  Returns the attribute at a given path, relative to this prim.
- [func hasAttribute(named: USDToken) -> Bool](./hasattribute%28named%29.md)
  Returns true if an attribute with a given name exists on this prim.
- [func makeAttribute(named: USDToken, as: USDPrim.Attribute.ValueType, custom: Bool, variability: USDPrim.Property.Variability) -> USDPrim.Attribute](./makeattribute%28named,as,custom,variability%29.md)
  Creates an attribute with the given name on this prim, or returns the existing attribute if one already exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute)*