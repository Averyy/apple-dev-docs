# tokens

**Framework**: UIKit  
**Kind**: property

The collection of tokens in the search text field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tokens: [UISearchToken] { get set }
```

#### Discussion

Use this property to access existing tokens, or to replace all tokens at once. To convert text in the search field into a token, use [`replaceTextualPortion(of:with:at:)`](uisearchtextfield/replacetextualportion(of:with:at:).md).

## See Also

- [func insertToken(UISearchToken, at: Int)](uisearchtextfield/inserttoken(_:at:).md)
  Adds a search token at a specific index.
- [func removeToken(at: Int)](uisearchtextfield/removetoken(at:).md)
  Removes a particular search token from the search text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/tokens)*