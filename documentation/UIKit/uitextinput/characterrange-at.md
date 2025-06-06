# characterRange(at:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the character or range of characters that is at a specified point in a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func characterRange(at point: CGPoint) -> UITextRange?
```

#### Return Value

An object representing a range that encloses a character (or characters) at `point`.

## Parameters

- `point`: A point in the view that is drawing a document’s text.

## See Also

- [func firstRect(for: UITextRange) -> CGRect](uitextinput/firstrect(for:).md)
  Returns the first rectangle that encloses a range of text in a document.
- [func closestPosition(to: CGPoint) -> UITextPosition?](uitextinput/closestposition(to:).md)
  Returns the position in a document that is closest to a specified point.
- [func selectionRects(for: UITextRange) -> [UITextSelectionRect]](uitextinput/selectionrects(for:).md)
  Returns an array of selection rects corresponding to the range of text.
- [func closestPosition(to: CGPoint, within: UITextRange) -> UITextPosition?](uitextinput/closestposition(to:within:).md)
  Returns the position in a document that is closest to a specified point in a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/characterrange(at:))*