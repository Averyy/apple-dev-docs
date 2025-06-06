# tokens(in:)

**Framework**: UIKit  
**Kind**: method

Returns the search field’s tokens that are within a given range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func tokens(in textRange: UITextRange) -> [UISearchToken]
```

#### Return Value

The tokens contained within the provided range.

#### Discussion

Use this method to find out which tokens are included in the user’s current selection. You can provide a range that spans a mixture of tokens and text.

## Parameters

- `textRange`: The range specifying a subset of the tokens.

## See Also

- [var tokenBackgroundColor: UIColor!](uisearchtextfield/tokenbackgroundcolor.md)
  The background color for all tokens in the search text field.
- [func positionOfToken(at: Int) -> UITextPosition](uisearchtextfield/positionoftoken(at:).md)
  Converts a token index into a text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/tokens(in:))*