# selectionRects(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns an array of selection rects corresponding to the range of text.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func selectionRects(for range: UITextRange) -> [UITextSelectionRect]
```

#### Return Value

An array of [`UITextSelectionRect`](uitextselectionrect.md) objects that encompass the selection.

## Parameters

- `range`: An object representing a range in a document’s text.

## See Also

- [func firstRect(for: UITextRange) -> CGRect](uitextinput/firstrect(for:).md)
  Returns the first rectangle that encloses a range of text in a document.
- [func closestPosition(to: CGPoint) -> UITextPosition?](uitextinput/closestposition(to:).md)
  Returns the position in a document that is closest to a specified point.
- [func closestPosition(to: CGPoint, within: UITextRange) -> UITextPosition?](uitextinput/closestposition(to:within:).md)
  Returns the position in a document that is closest to a specified point in a specified range.
- [func characterRange(at: CGPoint) -> UITextRange?](uitextinput/characterrange(at:).md)
  Returns the character or range of characters that is at a specified point in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/selectionrects(for:))*