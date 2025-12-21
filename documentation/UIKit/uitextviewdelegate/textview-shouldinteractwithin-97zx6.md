# textView(_:shouldInteractWith:in:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: UITextView, shouldInteractWith textAttachment: NSTextAttachment, in characterRange: NSRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if interaction with the text attachment should be allowed; [`false`](https://developer.apple.com/documentation/Swift/false) if interaction should not be allowed.

#### Discussion

A text view calls this method if the user taps or long-presses the text attachment and its [`image`](nstextattachment/image.md) property is not `nil`. Implementation of this method is optional. You can use this method to trigger an action in addition to displaying the text attachment inline with the text.

## Parameters

- `textView`: The text view containing the text attachment.
- `textAttachment`: The text attachment.
- `characterRange`: The character range containing the text attachment.

## See Also

- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:)-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [enum UITextItemInteraction](uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:)-97zx6)*