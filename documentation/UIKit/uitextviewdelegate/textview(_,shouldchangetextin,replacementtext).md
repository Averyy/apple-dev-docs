# textView(_:shouldChangeTextIn:replacementText:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to replace the specified text in the text view.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

## Declaration

```swift
optional func textView(_ textView: UITextView, shouldChangeTextIn range: NSRange, replacementText text: String) -> Bool
```

```objc
- (BOOL) textView:(UITextView *) textView shouldChangeTextInRange:(NSRange) range replacementText:(NSString *) text;
```

## Return Value

[`true`](../../Swift/true.md) if the old text should be replaced by the new text; [`false`](../../Swift/false.md) if the replacement operation should be aborted.

## Discussion

The text view calls this method whenever the user types a new character or deletes an existing character. Implementation of this method is optional. You can use this method to replace text before it is committed to the text view storage. For example, a spell checker might use this method to replace a misspelled word with the correct spelling.

## Parameters

- `textView`: The text view containing the changes.
- `range`: The current selection range. If the length of the range is 0, `range` reflects the current insertion point. If the user presses the Delete key, the length of the range is 1 and an empty string object replaces that single character.
- `text`: The text to insert.

## See Also

### Deprecated
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](./textview%28_,shouldinteractwith,in,interaction%29-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](./textview%28_,shouldinteractwith,in%29-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](./textview%28_,shouldinteractwith,in%29-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [enum UITextItemInteraction](../uitextiteminteraction.md)
  Constants that indicate the type of interaction the user expects to have with a URL or text attachment.
- [func textView(UITextView, editMenuForTextIn: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?](./textview%28_,editmenufortextin,suggestedactions%29.md)
  Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldchangetextin:replacementtext:))*