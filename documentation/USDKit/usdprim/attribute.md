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
- [USDPrim.Attribute.MetadataValue](usdprim/attribute/metadatavalue.md)
  A value that can be stored as metadata in a Universal Scene Description file.
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
  A value that can be stored on an attribute in a Universal Scene Description file.
### Structures
- [USDPrim.Attribute.Spec](usdprim/attribute/spec.md)
  A handle to an attribute definition stored in a layer.
- [USDPrim.Attribute.ValueType](usdprim/attribute/valuetype.md)
### Initializers
- [init()](usdprim/attribute/init.md)
  An invalid attribute handle.
- [init?(USDStage.Object)](usdprim/attribute/init(_:)-8gu7p.md)
  Casts an object handle to an attribute handle.
- [init?(USDPrim.Property)](usdprim/attribute/init(_:)-8mm8c.md)
  Casts a property handle to an attribute handle.
### Instance Properties
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
- [var stage: USDStage](usdprim/attribute/stage.md)
  The stage that owns this attribute.
- [var typeName: USDPrim.Attribute.ValueType](usdprim/attribute/typename.md)
- [var variability: USDPrim.Property.Variability](usdprim/attribute/variability.md)
### Default Implementations
- [CustomStringConvertible Implementations](usdprim/attribute/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [USDStage.Object.MetadataCollection](usdstage-4sfi1/object/metadatacollection.md)

## See Also

- [var attributes: [USDPrim.Attribute]](usdprim/attributes.md)
- [var authoredAttributes: [USDPrim.Attribute]](usdprim/authoredattributes.md)
- [func attribute(named: USDToken) -> USDPrim.Attribute](usdprim/attribute(named:).md)
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdprim/attribute(at:).md)
- [func hasAttribute(named: USDToken) -> Bool](usdprim/hasattribute(named:).md)
- [func makeAttribute(named: USDToken, as: USDPrim.Attribute.ValueType, custom: Bool, variability: USDPrim.Property.Variability) -> USDPrim.Attribute](usdprim/makeattribute(named:as:custom:variability:).md)
- [subscript<T>(USDToken, as _: T.Type) -> T?](usdprim/subscript(_:as:).md)
  Access or modify the value of a named attribute on this prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute)*