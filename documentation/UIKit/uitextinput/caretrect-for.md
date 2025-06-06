# caretRect(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a rectangle to draw the caret at a specified insertion point.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func caretRect(for position: UITextPosition) -> CGRect
```

#### Return Value

A rectangle that defines the area for drawing the caret.

#### Discussion

The system uses this value to calculate the length of the beam—the vertical line representing the pointer—when using a trackpad to interact with a text input area. You must implement this method even if text never becomes editable, and an insertion point caret never appears.

## Parameters

- `position`: An object that identifies a location in a text input area.

## See Also

- [func firstRect(for: UITextRange) -> CGRect](uitextinput/firstrect(for:).md)
  Returns the first rectangle that encloses a range of text in a document.
- [UIPointerShape.verticalBeam(length:)](uipointershape-swift.enum/verticalbeam(length:).md)
  The pointer morphs into a vertical beam using the specified length.
- [func caretTransform(for: UITextPosition) -> CGAffineTransform](uitextinput/carettransform(for:).md)
  Returns the transform to apply to the caret prior to drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/caretrect(for:))*