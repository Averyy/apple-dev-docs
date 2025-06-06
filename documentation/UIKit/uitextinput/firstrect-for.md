# firstRect(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the first rectangle that encloses a range of text in a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func firstRect(for range: UITextRange) -> CGRect
```

#### Return Value

The first rectangle in a `range` of text. You might use this rectangle to draw a correction rectangle. The “first” in the name refers the rectangle enclosing the first line when the range encompasses multiple lines of text.

## Parameters

- `range`: An object that represents a range of text in a document.

## See Also

- [func caretRect(for: UITextPosition) -> CGRect](uitextinput/caretrect(for:).md)
  Returns a rectangle to draw the caret at a specified insertion point.
- [func closestPosition(to: CGPoint) -> UITextPosition?](uitextinput/closestposition(to:).md)
  Returns the position in a document that is closest to a specified point.
- [func selectionRects(for: UITextRange) -> [UITextSelectionRect]](uitextinput/selectionrects(for:).md)
  Returns an array of selection rects corresponding to the range of text.
- [func closestPosition(to: CGPoint, within: UITextRange) -> UITextPosition?](uitextinput/closestposition(to:within:).md)
  Returns the position in a document that is closest to a specified point in a specified range.
- [func characterRange(at: CGPoint) -> UITextRange?](uitextinput/characterrange(at:).md)
  Returns the character or range of characters that is at a specified point in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/firstrect(for:))*