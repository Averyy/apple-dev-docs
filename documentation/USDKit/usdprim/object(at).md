# object(at:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns the object at a given path, relative to this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func object(at path: USDLayer.Path) -> USDStage.Object
```

## Discussion

If `path` is relative, it is anchored to this prim’s path. If no object exists at the resolved path, returns an invalid object handle.

## See Also

### Accessing properties
- [var properties: [USDPrim.Property]](./properties.md)
  The properties of this prim, including those provided by its schemas.
- [var authoredProperties: [USDPrim.Property]](./authoredproperties.md)
  The properties of this prim that have an authored opinion.
- [var propertyNames: [USDToken]](./propertynames.md)
  The names of this prim’s properties, including those provided by its schemas.
- [var authoredPropertyNames: [USDToken]](./authoredpropertynames.md)
  The names of this prim’s properties that have an authored opinion.
- [func property(named: USDToken) -> USDPrim.Property](./property%28named%29.md)
  Returns the property with a given name on this prim.
- [func hasProperty(named: USDToken) -> Bool](./hasproperty%28named%29.md)
  Returns true if an attribute or relationship with a given name exists.
- [USDPrim.Property](./property.md)
  A named property on a prim, which is either an attribute or a relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/object(at:))*