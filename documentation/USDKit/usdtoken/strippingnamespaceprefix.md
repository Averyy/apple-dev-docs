# strippingNamespacePrefix(_:)

**Framework**: USDKit  
**Kind**: method

Returns this token with the given namespace prefix removed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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

- [func strippingLeadingNamespace() -> USDToken](usdtoken/strippingleadingnamespace.md)
  Returns this token with its leading namespace component removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtoken/strippingnamespaceprefix(_:))*