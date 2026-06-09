# strippingLeadingNamespace()

**Framework**: USDKit  
**Kind**: method

Returns this token with its leading namespace component removed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func strippingLeadingNamespace() -> USDToken
```

#### Return Value

The token with its leading namespace stripped, or the empty token if no namespace component exists.

## See Also

- [func strippingNamespacePrefix(USDToken) -> USDToken?](usdtoken/strippingnamespaceprefix(_:).md)
  Returns this token with the given namespace prefix removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtoken/strippingleadingnamespace())*