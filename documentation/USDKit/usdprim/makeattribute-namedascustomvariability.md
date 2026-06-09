# makeAttribute(named:as:custom:variability:)

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
@discardableResult
func makeAttribute(named name: USDToken, as type: USDPrim.Attribute.ValueType, custom: Bool = true, variability: USDPrim.Property.Variability = .varying) -> USDPrim.Attribute
```

## See Also

- [var attributes: [USDPrim.Attribute]](usdprim/attributes.md)
- [var authoredAttributes: [USDPrim.Attribute]](usdprim/authoredattributes.md)
- [func attribute(named: USDToken) -> USDPrim.Attribute](usdprim/attribute(named:).md)
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdprim/attribute(at:).md)
- [func hasAttribute(named: USDToken) -> Bool](usdprim/hasattribute(named:).md)
- [subscript<T>(USDToken, as _: T.Type) -> T?](usdprim/subscript(_:as:).md)
  Access or modify the value of a named attribute on this prim.
- [USDPrim.Attribute](usdprim/attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/makeattribute(named:as:custom:variability:))*