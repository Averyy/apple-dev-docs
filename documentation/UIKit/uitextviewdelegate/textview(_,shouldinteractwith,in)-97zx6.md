# textView(_:shouldInteractWith:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 10.0

> **Deprecated**: Use [`textView(_:shouldInteractWith:in:interaction:)`](./textview%28_,shouldinteractwith,in,interaction%29-5qha9.md) instead.

## Declaration

```swift
optional func textView(_ textView: UITextView, shouldInteractWith textAttachment: NSTextAttachment, in characterRange: NSRange) -> Bool
```

```objc
- (BOOL) textView:(UITextView *) textView shouldInteractWithTextAttachment:(NSTextAttachment *) textAttachment inRange:(NSRange) characterRange;
```

## Return Value

[`true`](../../Swift/true.md) if interaction with the text attachment should be allowed; [`false`](../../Swift/false.md) if interaction should not be allowed.

## Discussion

A text view calls this method if the user taps or long-presses the text attachment and its [`image`](../nstextattachment/image.md) property is not `nil`. Implementation of this method is optional. You can use this method to trigger an action in addition to displaying the text attachment inline with the text.

## Parameters

- `textView`: The text view containing the text attachment.
- `textAttachment`: The text attachment.
- `characterRange`: The character range containing the text attachment.

## See Also

### Deprecated
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](./textview%28_,shouldinteractwith,in%29-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [enum UITextItemInteraction](../uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.
- [func textView(UITextView, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./textview%28_,shouldchangetextin,replacementtext%29.md)
  Asks the delegate whether to replace the specified text in the text view.
- [func textView(UITextView, editMenuForTextIn: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?](./textview%28_,editmenufortextin,suggestedactions%29.md)
  Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:)-97zx6)*