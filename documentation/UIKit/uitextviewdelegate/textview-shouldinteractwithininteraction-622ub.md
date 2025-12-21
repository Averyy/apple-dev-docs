# textView(_:shouldInteractWith:in:interaction:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textView(_ textView: UITextView, shouldInteractWith URL: URL, in characterRange: NSRange, interaction: UITextItemInteraction) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if interaction with the URL should be allowed; [`false`](https://developer.apple.com/documentation/Swift/false) if interaction should not be allowed.

#### Discussion

This method is called on only the first interaction with the URL link. For example, this method is called when the user wants their first interaction with a URL to display a list of actions they can take; if the user chooses an open action from the list, this method is not called, because “open” represents the second interaction with the same URL.

> ❗ **Important**:  Links in text views are interactive only if the text view is selectable but noneditable. That is, if the value of the [`UITextView`](uitextview.md) [`isSelectable`](uitextview/isselectable.md) property is [`true`](https://developer.apple.com/documentation/Swift/true) and the [`isEditable`](uitextview/iseditable.md) property is [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `textView`: The text view containing the text attachment.
- `URL`: The URL to be processed.
- `characterRange`: The character range containing the URL.
- `interaction`: The type of interaction that is occurring (for possible values, see  ).

## See Also

- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:)-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:)-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [enum UITextItemInteraction](uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-622ub)*