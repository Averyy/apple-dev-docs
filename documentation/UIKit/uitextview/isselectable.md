# isSelectable

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the text view is selectable.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isSelectable: Bool { get set }
```

```objc
@property (nonatomic, getter=isSelectable) BOOL selectable;
```

## Discussion

This property controls the ability of the user to select content and interact with URLs and text attachments. The default value is [`true`](../../Swift/true.md).

## See Also

### Working with the selection
- [func scrollRangeToVisible(NSRange)](./scrollrangetovisible%28_%29.md)
  Scrolls the text view until the text in the specified range is visible.
- [var clearsOnInsertion: Bool](./clearsoninsertion.md)
  A Boolean value that indicates whether inserting text replaces the previous contents.
- [var selectedRange: NSRange](./selectedrange.md)
  The current selection range of the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/isselectable)*