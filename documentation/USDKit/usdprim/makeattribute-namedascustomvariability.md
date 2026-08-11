# makeAttribute(named:as:custom:variability:)

**Framework**: USDKit  
**Kind**: method

Creates an attribute with the given name on this prim, or returns the existing attribute if one already exists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func makeAttribute(named name: USDToken, as type: USDPrim.Attribute.ValueType, custom: Bool = true, variability: USDPrim.Property.Variability = .varying) -> USDPrim.Attribute
```

#### Return Value

The attribute with the given name.

## Parameters

- `name`: The name of the attribute to create.
- `type`: The value type of the attribute.
- `custom`: A Boolean value that indicates whether the attribute is a custom attribute not defined by a schema.
- `variability`: The variability of the attribute.

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
- [USDPrim.Attribute](usdprim/attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/makeattribute(named:as:custom:variability:))*