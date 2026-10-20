# attributes

**Framework**: USDKit  
**Kind**: property  
**Role**: Instance Property

The attributes of this prim, including those provided by its schemas.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var attributes: [USDPrim.Attribute] { get }
```

## See Also

### Accessing attributes
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
- [USDPrim.Attribute](./attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attributes)*