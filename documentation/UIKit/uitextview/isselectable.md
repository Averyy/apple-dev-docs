# isSelectable

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the text view is selectable.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isSelectable: Bool { get set }
```

#### Discussion

This property controls the ability of the user to select content and interact with URLs and text attachments. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var selectedRange: NSRange](uitextview/selectedrange.md)
  The current selection range of the text view.
- [func scrollRangeToVisible(NSRange)](uitextview/scrollrangetovisible(_:).md)
  Scrolls the text view until the text in the specified range is visible.
- [var clearsOnInsertion: Bool](uitextview/clearsoninsertion.md)
  A Boolean value that indicates whether inserting text replaces the previous contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/isselectable)*