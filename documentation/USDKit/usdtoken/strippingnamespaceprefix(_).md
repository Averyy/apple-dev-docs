# strippingNamespacePrefix(_:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns this token with the given namespace prefix removed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func strippingNamespacePrefix(_ prefix: USDToken) -> USDToken?
```

#### Return Value

The token with `prefix` removed, or `nil` if the prefix does not match.

#### Discussion

Matching is done at namespace boundaries.

## Parameters

- `prefix`: The namespace prefix to strip.

## See Also

### Stripping namespaces
- [func strippingLeadingNamespace() -> USDToken](./strippingleadingnamespace%28%29.md)
  Returns this token with its leading namespace component removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtoken/strippingnamespaceprefix(_:))*