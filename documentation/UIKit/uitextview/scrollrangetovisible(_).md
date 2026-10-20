# scrollRangeToVisible(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the text view until the text in the specified range is visible.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func scrollRangeToVisible(_ range: NSRange)
```

```objc
- (void) scrollRangeToVisible:(NSRange) range;
```

## Parameters

- `range`: The range of text to scroll into view.

## See Also

### Working with the selection
- [var clearsOnInsertion: Bool](./clearsoninsertion.md)
  A Boolean value that indicates whether inserting text replaces the previous contents.
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value that indicates whether the text view is selectable.
- [var selectedRange: NSRange](./selectedrange.md)
  The current selection range of the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/scrollrangetovisible(_:))*