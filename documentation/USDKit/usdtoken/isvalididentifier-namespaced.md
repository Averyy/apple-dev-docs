# isValidIdentifier(_:namespaced:)

**Framework**: USDKit  
**Kind**: method

Returns a Boolean value that indicates whether the given string is a valid USD identifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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