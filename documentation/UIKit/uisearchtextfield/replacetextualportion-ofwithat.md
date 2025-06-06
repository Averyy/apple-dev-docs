# replaceTextualPortion(of:with:at:)

**Framework**: UIKit  
**Kind**: method

Converts text in a search field into a search token.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func replaceTextualPortion(of textRange: UITextRange, with token: UISearchToken, at tokenIndex: Int)
```

#### Discussion

This method removes any text in the specified range, inserts the provided token at the specified index, and selects the newly inserted token. Prefer using this convenience method over performing each step with other methods. When your app calls [`replaceTextualPortion(of:with:at:)`](uisearchtextfield/replacetextualportion(of:with:at:).md), UIKit commits any marked text before modifying the text, and creates a single undo group.

This method doesn’t remove any tokens in the `textRange`, so you don’t have to manually trim the [`selectedTextRange`](uitextinput/selectedtextrange.md) before you use it in this method.

## Parameters

- `textRange`: The text to remove.
- `token`: The token to add.
- `tokenIndex`: The location for the added token.

## See Also

- [var textualRange: UITextRange](uisearchtextfield/textualrange.md)
  The range of the field’s text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/replacetextualportion(of:with:at:))*