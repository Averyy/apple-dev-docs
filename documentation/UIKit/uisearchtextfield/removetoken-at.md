# removeToken(at:)

**Framework**: UIKit  
**Kind**: method

Removes a particular search token from the search text field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeToken(at tokenIndex: Int)
```

## Parameters

- `tokenIndex`: Within the   array, the index of the token you want to remove.

## See Also

- [var tokens: [UISearchToken]](uisearchtextfield/tokens.md)
  The collection of tokens in the search text field.
- [func insertToken(UISearchToken, at: Int)](uisearchtextfield/inserttoken(_:at:).md)
  Adds a search token at a specific index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/removetoken(at:))*