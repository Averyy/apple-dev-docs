# clearsOnInsertion

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether inserting text replaces the previous contents.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var clearsOnInsertion: Bool { get set }
```

```objc
@property (nonatomic) BOOL clearsOnInsertion;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md). When the value of this property is [`true`](../../Swift/true.md) and the text view is in editing mode, the selection UI is hidden and inserting new text clears the contents of the text view and sets the value of this property back to [`false`](../../Swift/false.md).

## See Also

### Working with the selection
- [func scrollRangeToVisible(NSRange)](./scrollrangetovisible%28_%29.md)
  Scrolls the text view until the text in the specified range is visible.
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value that indicates whether the text view is selectable.
- [var selectedRange: NSRange](./selectedrange.md)
  The current selection range of the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/clearsoninsertion)*