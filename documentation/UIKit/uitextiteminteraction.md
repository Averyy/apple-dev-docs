# UITextItemInteraction

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the type of interaction the user expects to have with a URL or text attachment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum UITextItemInteraction
```

## Topics

### Constants
- [UITextItemInteraction.invokeDefaultAction](uitextiteminteraction/invokedefaultaction.md)
  The user wants to perform the default action on the text item; for example, opening a URL.
- [UITextItemInteraction.presentActions](uitextiteminteraction/presentactions.md)
  The user wants to be presented with a list of actions that can be taken on the text item, such as opening the link in a different way or downloading content from the link.
- [UITextItemInteraction.preview](uitextiteminteraction/preview.md)
  The user wants to get a preview of the content represented by the text item, such as by initiating a peek and pop on a link.
### Initializers
- [init?(rawValue: Int)](uitextiteminteraction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-5qha9.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange, interaction: UITextItemInteraction) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-622ub.md)
  Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.
- [func textView(UITextView, shouldInteractWith: NSTextAttachment, in: NSRange) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:)-97zx6.md)
  Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text.
- [func textView(UITextView, shouldInteractWith: URL, in: NSRange) -> Bool](uitextviewdelegate/textview(_:shouldinteractwith:in:)-98tho.md)
  Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextiteminteraction)*