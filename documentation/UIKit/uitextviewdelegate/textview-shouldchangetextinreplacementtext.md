# textView(_:shouldChangeTextIn:replacementText:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to replace the specified text in the text view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textView(_ textView: UITextView, shouldChangeTextIn range: NSRange, replacementText text: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the old text should be replaced by the new text; [`false`](https://developer.apple.com/documentation/swift/false) if the replacement operation should be aborted.

#### Discussion

The text view calls this method whenever the user types a new character or deletes an existing character. Implementation of this method is optional. You can use this method to replace text before it is committed to the text view storage. For example, a spell checker might use this method to replace a misspelled word with the correct spelling.

## Parameters

- `textView`: The text view containing the changes.
- `range`: The current selection range. If the length of the range is 0,   reflects the current insertion point. If the user presses the Delete key, the length of the range is 1 and an empty string object replaces that single character.
- `text`: The text to insert.

## See Also

- [func textViewDidChange(UITextView)](uitextviewdelegate/textviewdidchange(_:).md)
  Tells the delegate when the user changes the text or attributes in the specified text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldchangetextin:replacementtext:))*