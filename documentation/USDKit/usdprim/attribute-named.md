# attribute(named:)

**Framework**: USDKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func attribute(named name: USDToken) -> USDPrim.Attribute
```

## See Also

- [var attributes: [USDPrim.Attribute]](usdprim/attributes.md)
- [var authoredAttributes: [USDPrim.Attribute]](usdprim/authoredattributes.md)
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdprim/attribute(at:).md)
- [func hasAttribute(named: USDToken) -> Bool](usdprim/hasattribute(named:).md)
- [func makeAttribute(named: USDToken, as: USDPrim.Attribute.ValueType, custom: Bool, variability: USDPrim.Property.Variability) -> USDPrim.Attribute](usdprim/makeattribute(named:as:custom:variability:).md)
- [subscript<T>(USDToken, as _: T.Type) -> T?](usdprim/subscript(_:as:).md)
  Access or modify the value of a named attribute on this prim.
- [USDPrim.Attribute](usdprim/attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute(named:))*