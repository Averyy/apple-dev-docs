# textView(_:shouldInteractWith:in:interaction:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.

**Availability**:
- iOS 10.0+ - Deprecated in 17.0
- iPadOS 10.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS 10.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use text item methods in [`UITextViewDelegate`](../uitextviewdelegate.md) instead.

## Declaration

```swift
optional func textView(_ textView: UITextView, shouldInteractWith URL: URL, in characterRange: NSRange, interaction: UITextItemInteraction) -> Bool
```

```objc
- (BOOL) textView:(UITextView *) textView shouldInteractWithURL:(NSURL *) URL inRange:(NSRange) characterRange interaction:(UITextItemInteraction) interaction;
```

#### Return Value

[`true`](../../Swift/true.md) if interaction with the URL should be allowed; [`false`](../../Swift/false.md) if interaction should not be allowed.

#### Discussion

This method is called on only the first interaction with the URL link. For example, this method is called when the user wants their first interaction with a URL to display a list of actions they can take; if the user chooses an open action from the list, this method is not called, because “open” represents the second interaction with the same URL.

> ❗ **Important**:  Links in text views are interactive only if the text view is selectable but noneditable. That is, if the value of the [`UITextView`](../uitextview.md) [`isSelectable`](../uitextview/isselectable.md) property is [`true`](../../Swift/true.md) and the [`isEditable`](../uitextview/iseditable.md) property is [`false`](../../Swift/false.md).

## Parameters

- `textView`: The text view containing the text attachment.
- `URL`: The URL to be processed.
- `characterRange`: The character range containing the URL.
- `interaction`: The type of interaction that is occurring (for possible values, see [`UITextItemInteraction`](../uitextiteminteraction.md)).

## See Also

### Deprecated
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](./textview%28_,shouldinteractwith,in%29-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](./textview%28_,shouldinteractwith,in%29-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [enum UITextItemInteraction](../uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.
- [func textView(UITextView, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./textview%28_,shouldchangetextin,replacementtext%29.md)
  Asks the delegate whether to replace the specified text in the text view.
- [func textView(UITextView, editMenuForTextIn: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?](./textview%28_,editmenufortextin,suggestedactions%29.md)
  Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-622ub)*