# init(validating:)

**Framework**: USDKit  
**Kind**: init

Creates a path from its string representation, validating that `path` is well-formed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init?(validating path: String)
```

#### Return Value

`nil` if `path` cannot be parsed as a USD path expression.

## Parameters

- `path`: The path string to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/path/init(validating:))*