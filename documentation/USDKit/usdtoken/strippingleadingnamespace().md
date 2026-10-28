# strippingLeadingNamespace()

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns this token with its leading namespace component removed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func strippingLeadingNamespace() -> USDToken
```

## Return Value

The token with its leading namespace stripped, or the empty token if no namespace component exists.

## See Also

### Stripping namespaces
- [func strippingNamespacePrefix(USDToken) -> USDToken?](./strippingnamespaceprefix%28_%29.md)
  Returns this token with the given namespace prefix removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtoken/strippingleadingnamespace())*