# textView(_:shouldInteractWith:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 10.0

> **Deprecated**: Use [`textView(_:shouldInteractWith:in:interaction:)`](./textview%28_,shouldinteractwith,in,interaction%29-622ub.md) instead.

## Declaration

```swift
optional func textView(_ textView: UITextView, shouldInteractWith URL: URL, in characterRange: NSRange) -> Bool
```

```objc
- (BOOL) textView:(UITextView *) textView shouldInteractWithURL:(NSURL *) URL inRange:(NSRange) characterRange;
```

## Return Value

[`true`](../../Swift/true.md) if interaction with the URL should be allowed; [`false`](../../Swift/false.md) if interaction should not be allowed.

## Discussion

The text view calls this method if the user taps or long-presses the URL link. Implementation of this method is optional. By default, the text view opens the application responsible for handling the URL type and passes it the URL. You can use this method to trigger an alternative action, such as displaying the web content at the URL in a web view within the current application.

> ❗ **Important**:  Links in text views are interactive only if the text view is selectable but noneditable. That is, if the value of the `UITextView` [`isSelectable`](../uitextview/isselectable.md) property is [`true`](../../Swift/true.md) and the [`isEditable`](../uitextview/iseditable.md) property is [`false`](../../Swift/false.md).

## Parameters

- `textView`: The text view containing the text attachment.
- `URL`: The URL to be processed.
- `characterRange`: The character range containing the URL.

## See Also

### Deprecated
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](./textview%28_,shouldinteractwith,in%29-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [enum UITextItemInteraction](../uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.
- [func textView(UITextView, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./textview%28_,shouldchangetextin,replacementtext%29.md)
  Asks the delegate whether to replace the specified text in the text view.
- [func textView(UITextView, editMenuForTextIn: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?](./textview%28_,editmenufortextin,suggestedactions%29.md)
  Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:)-98tho)*