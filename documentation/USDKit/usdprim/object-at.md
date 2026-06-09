# object(at:)

**Framework**: USDKit  
**Kind**: method

Returns the object at a given path, relative to this prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func object(at path: USDLayer.Path) -> USDStage.Object
```

#### Discussion

If `path` is relative, it is anchored to this prim’s path. If no object exists at the resolved path, returns an invalid object handle.

## See Also

- [var properties: [USDPrim.Property]](usdprim/properties.md)
- [var authoredProperties: [USDPrim.Property]](usdprim/authoredproperties.md)
- [var propertyNames: [USDToken]](usdprim/propertynames.md)
- [var authoredPropertyNames: [USDToken]](usdprim/authoredpropertynames.md)
- [func property(named: USDToken) -> USDPrim.Property](usdprim/property(named:).md)
- [func hasProperty(named: USDToken) -> Bool](usdprim/hasproperty(named:).md)
- [USDPrim.Property](usdprim/property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/object(at:))*