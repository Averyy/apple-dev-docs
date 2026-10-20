# UITextItemInteraction

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the type of interaction the user expects to have with a URL or text attachment.

**Availability**:
- iOS 10.0+ - Deprecated in 17.0
- iPadOS 10.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS 10.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use text item methods in [`UITextViewDelegate`](./uitextviewdelegate.md) instead.

## Declaration

```swift
enum UITextItemInteraction
```

```c
enum UITextItemInteraction : NSInteger;
```

## Topics

### Constants
- [UITextItemInteraction.invokeDefaultAction](./uitextiteminteraction/invokedefaultaction.md)
  The user wants to perform the default action on the text item; for example, opening a URL.
- [UITextItemInteraction.presentActions](./uitextiteminteraction/presentactions.md)
  The user wants to be presented with a list of actions that can be taken on the text item, such as opening the link in a different way or downloading content from the link.
- [UITextItemInteraction.preview](./uitextiteminteraction/preview.md)
  The user wants to get a preview of the content represented by the text item, such as by initiating a peek and pop on a link.
### Initializers
- [init?(rawValue: Int)](./uitextiteminteraction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](./uitextviewdelegate/textview%28_,shouldinteractwith,in,interaction%29-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](./uitextviewdelegate/textview%28_,shouldinteractwith,in,interaction%29-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](./uitextviewdelegate/textview%28_,shouldinteractwith,in%29-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](./uitextviewdelegate/textview%28_,shouldinteractwith,in%29-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./uitextviewdelegate/textview%28_,shouldchangetextin,replacementtext%29.md)
  Asks the delegate whether to replace the specified text in the text view.
- [func textView(UITextView, editMenuForTextIn: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?](./uitextviewdelegate/textview%28_,editmenufortextin,suggestedactions%29.md)
  Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextiteminteraction)*