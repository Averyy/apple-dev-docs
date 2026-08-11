# hasProperty(named:)

**Framework**: USDKit  
**Kind**: method

Returns true if an attribute or relationship with a given name exists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func hasProperty(named name: USDToken) -> Bool
```

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
- [func object(at: USDLayer.Path) -> USDStage.Object](usdprim/object(at:).md)
  Returns the object at a given path, relative to this prim.
- [USDPrim.Property](usdprim/property.md)
  A named property on a prim, which is either an attribute or a relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/hasproperty(named:))*