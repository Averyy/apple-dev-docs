# characterRange(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the character or range of characters that is at a specified point in a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func characterRange(at point: CGPoint) -> UITextRange?
```

```objc
- (UITextRange *) characterRangeAtPoint:(CGPoint) point;
```

## Return Value

An object representing a range that encloses a character (or characters) at `point`.

## Parameters

- `point`: A point in the view that is drawing a document’s text.

## See Also

### Working with geometry and hit-testing
- [func firstRect(for: UITextRange) -> CGRect](./firstrect%28for%29.md)
  Returns the first rectangle that encloses a range of text in a document.
- [func closestPosition(to: CGPoint) -> UITextPosition?](./closestposition%28to%29.md)
  Returns the position in a document that is closest to a specified point.
- [func selectionRects(for: UITextRange) -> [UITextSelectionRect]](./selectionrects%28for%29.md)
  Returns an array of selection rects corresponding to the range of text.
- [func closestPosition(to: CGPoint, within: UITextRange) -> UITextPosition?](./closestposition%28to,within%29.md)
  Returns the position in a document that is closest to a specified point in a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/characterrange(at:))*