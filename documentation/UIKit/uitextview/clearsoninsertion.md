# clearsOnInsertion

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether inserting text replaces the previous contents.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var clearsOnInsertion: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) and the text view is in editing mode, the selection UI is hidden and inserting new text clears the contents of the text view and sets the value of this property back to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var selectedRange: NSRange](uitextview/selectedrange.md)
  The current selection range of the text view.
- [func scrollRangeToVisible(NSRange)](uitextview/scrollrangetovisible(_:).md)
  Scrolls the text view until the text in the specified range is visible.
- [var isSelectable: Bool](uitextview/isselectable.md)
  A Boolean value that indicates whether the text view is selectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/clearsoninsertion)*