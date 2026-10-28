# selectedRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current selection range of the text view.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

## Declaration

```swift
var selectedRange: NSRange { get set }
```

```objc
@property (nonatomic) NSRange selectedRange;
```

## Discussion

In iOS 2.2 and earlier, the length of the selection range is always 0, indicating that the selection is actually an insertion point. In iOS 3.0 and later, the length of the selection range may be non-zero.

## See Also

### Working with the selection
- [func scrollRangeToVisible(NSRange)](./scrollrangetovisible%28_%29.md)
  Scrolls the text view until the text in the specified range is visible.
- [var clearsOnInsertion: Bool](./clearsoninsertion.md)
  A Boolean value that indicates whether inserting text replaces the previous contents.
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value that indicates whether the text view is selectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/selectedrange)*