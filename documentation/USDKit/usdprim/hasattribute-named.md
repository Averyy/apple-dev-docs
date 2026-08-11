# hasAttribute(named:)

**Framework**: USDKit  
**Kind**: method

Returns true if an attribute with a given name exists on this prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func hasAttribute(named name: USDToken) -> Bool
```

## See Also

- [var attributes: [USDPrim.Attribute]](usdprim/attributes.md)
  The attributes of this prim, including those provided by its schemas.
- [var authoredAttributes: [USDPrim.Attribute]](usdprim/authoredattributes.md)
  The attributes of this prim that have an authored opinion.
- [func attribute(named: USDToken) -> USDPrim.Attribute](usdprim/attribute(named:).md)
  Returns the attribute with a given name on this prim.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdprim/attribute(at:).md)
  Returns the attribute at a given path, relative to this prim.
- [func makeAttribute(named: USDToken, as: USDPrim.Attribute.ValueType, custom: Bool, variability: USDPrim.Property.Variability) -> USDPrim.Attribute](usdprim/makeattribute(named:as:custom:variability:).md)
  Creates an attribute with the given name on this prim, or returns the existing attribute if one already exists.
- [USDPrim.Attribute](usdprim/attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/hasattribute(named:))*