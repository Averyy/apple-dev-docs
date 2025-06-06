# selectedRange

**Framework**: UIKit  
**Kind**: property

The current selection range of the text view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedRange: NSRange { get set }
```

#### Discussion

In iOS 2.2 and earlier, the length of the selection range is always 0, indicating that the selection is actually an insertion point. In iOS 3.0 and later, the length of the selection range may be non-zero.

## See Also

- [func scrollRangeToVisible(NSRange)](uitextview/scrollrangetovisible(_:).md)
  Scrolls the text view until the text in the specified range is visible.
- [var clearsOnInsertion: Bool](uitextview/clearsoninsertion.md)
  A Boolean value that indicates whether inserting text replaces the previous contents.
- [var isSelectable: Bool](uitextview/isselectable.md)
  A Boolean value that indicates whether the text view is selectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/selectedrange)*