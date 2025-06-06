# insertToken(_:at:)

**Framework**: UIKit  
**Kind**: method

Adds a search token at a specific index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func insertToken(_ token: UISearchToken, at tokenIndex: Int)
```

#### Discussion

If you’re converting part of the search field’s text into a token, use [`replaceTextualPortion(of:with:at:)`](uisearchtextfield/replacetextualportion(of:with:at:).md).

## Parameters

- `token`: The search token to be inserted.
- `tokenIndex`: Within the   array, the index at which to insert the token.

## See Also

- [var tokens: [UISearchToken]](uisearchtextfield/tokens.md)
  The collection of tokens in the search text field.
- [func removeToken(at: Int)](uisearchtextfield/removetoken(at:).md)
  Removes a particular search token from the search text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/inserttoken(_:at:))*