# shouldChangeText(in:replacementText:)

**Framework**: UIKit  
**Kind**: method

Asks whether to replace the text in the specified range.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func shouldChangeText(in range: UITextRange, replacementText text: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the text should be changed or [`false`](https://developer.apple.com/documentation/swift/false) if it should not.

#### Discussion

Prior to replacing text, this method is called to give your delegate a chance to accept or reject the edits. If you do not implement this method, the return value defaults to [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `range`: A range of text in a document.
- `text`: The proposed text to replace the text in  .

## See Also

- [func text(in: UITextRange) -> String?](uitextinput/text(in:).md)
  Returns the text in the specified range.
- [func replace(UITextRange, withText: String)](uitextinput/replace(_:withtext:).md)
  Replaces the text in a document that is in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/shouldchangetext(in:replacementtext:))*