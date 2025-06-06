# positionOfToken(at:)

**Framework**: UIKit  
**Kind**: method

Converts a token index into a text position.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func positionOfToken(at tokenIndex: Int) -> UITextPosition
```

#### Return Value

The text position of the token.

#### Discussion

Use this method to convert a token’s index in the [`tokens`](uisearchtextfield/tokens.md) array into the token’s [`UITextPosition`](uitextposition.md) in the overall contents of the text field. Many [`UITextInput`](uitextinput.md) methods for interacting with text take a [`UITextPosition`](uitextposition.md) or [`UITextRange`](uitextrange.md) (constructed from two text positions) as a parameter.

To select a search token, assign a [`UITextRange`](uitextrange.md) that contains the token’s position to the [`selectedTextRange`](uitextinput/selectedtextrange.md) property.

## Parameters

- `tokenIndex`: The array index of the token.

## See Also

- [var tokenBackgroundColor: UIColor!](uisearchtextfield/tokenbackgroundcolor.md)
  The background color for all tokens in the search text field.
- [func tokens(in: UITextRange) -> [UISearchToken]](uisearchtextfield/tokens(in:).md)
  Returns the search field’s tokens that are within a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/positionoftoken(at:))*