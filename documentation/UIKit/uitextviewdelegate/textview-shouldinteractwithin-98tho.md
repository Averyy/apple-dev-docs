# textView(_:shouldInteractWith:in:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: UITextView, shouldInteractWith URL: URL, in characterRange: NSRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if interaction with the URL should be allowed; [`false`](https://developer.apple.com/documentation/swift/false) if interaction should not be allowed.

#### Discussion

The text view calls this method if the user taps or long-presses the URL link. Implementation of this method is optional. By default, the text view opens the application responsible for handling the URL type and passes it the URL. You can use this method to trigger an alternative action, such as displaying the web content at the URL in a web view within the current application.

> ❗ **Important**:  Links in text views are interactive only if the text view is selectable but noneditable. That is, if the value of the `UITextView` [`isSelectable`](uitextview/isselectable.md) property is [`true`](https://developer.apple.com/documentation/swift/true) and the [`isEditable`](uitextview/iseditable.md) property is [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `textView`: The text view containing the text attachment.
- `URL`: The URL to be processed.
- `characterRange`: The character range containing the URL.

## See Also

- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:)-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [enum UITextItemInteraction](uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:)-98tho)*