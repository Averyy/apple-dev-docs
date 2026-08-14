# USDToken

**Framework**: USDKit  
**Kind**: struct

An interned, efficiently compared string that names prims, properties, and other scene-description identifiers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct USDToken
```

## Topics

### Creating a token
- [init()](usdtoken/init.md)
- [init(String)](usdtoken/init(_:).md)
- [init(namespaceComponents: [USDToken])](usdtoken/init(namespacecomponents:).md)
  Creates a namespaced token by joining `components` with `:`.
### Inspecting the token
- [var string: String](usdtoken/string.md)
- [var isEmpty: Bool](usdtoken/isempty.md)
- [var namespaceComponents: [USDToken]](usdtoken/namespacecomponents.md)
  The token split into its namespace components, separated by `:`.
### Stripping namespaces
- [func strippingLeadingNamespace() -> USDToken](usdtoken/strippingleadingnamespace.md)
  Returns this token with its leading namespace component removed.
- [func strippingNamespacePrefix(USDToken) -> USDToken?](usdtoken/strippingnamespaceprefix(_:).md)
  Returns this token with the given namespace prefix removed.
### Validating identifiers
- [static func isValidIdentifier(String, namespaced: Bool) -> Bool](usdtoken/isvalididentifier(_:namespaced:).md)
  Returns a Boolean value that indicates whether the given string is a valid USD identifier.

## Relationships

### Conforms To
- [Comparable](../swift/comparable.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](usdstage/object/metadatavalue.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [struct USDValue](usdvalue.md)
  A type-erased container for a value stored in a Universal Scene Description file.
- [protocol USDValueProtocol](usdvalueprotocol.md)
  A type that can be wrapped in a [`USDValue`](usdvalue.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtoken)*