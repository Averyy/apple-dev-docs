# scrollRangeToVisible(_:)

**Framework**: UIKit  
**Kind**: method

Scrolls the text view until the text in the specified range is visible.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func scrollRangeToVisible(_ range: NSRange)
```

## Parameters

- `range`: The range of text to scroll into view.

## See Also

- [var selectedRange: NSRange](uitextview/selectedrange.md)
  The current selection range of the text view.
- [var clearsOnInsertion: Bool](uitextview/clearsoninsertion.md)
  A Boolean value that indicates whether inserting text replaces the previous contents.
- [var isSelectable: Bool](uitextview/isselectable.md)
  A Boolean value that indicates whether the text view is selectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/scrollrangetovisible(_:))*