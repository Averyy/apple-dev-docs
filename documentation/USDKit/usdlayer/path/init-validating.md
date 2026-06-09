# init(validating:)

**Framework**: USDKit  
**Kind**: init

Creates a path from its string representation, validating that `path` is well-formed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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