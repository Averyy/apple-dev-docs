# isValidIdentifier(_:namespaced:)

**Framework**: USDKit  
**Kind**: method

Returns a Boolean value that indicates whether the given string is a valid USD identifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func isValidIdentifier(_ name: String, namespaced: Bool = false) -> Bool
```

#### Return Value

`true` if `name` is a valid identifier; otherwise, `false`.

## Parameters

- `name`: The string to evaluate.
- `namespaced`: Pass `true` to allow the `:` namespace separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtoken/isvalididentifier(_:namespaced:))*