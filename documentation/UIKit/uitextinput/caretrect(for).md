# caretRect(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a rectangle to draw the caret at a specified insertion point.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func caretRect(for position: UITextPosition) -> CGRect
```

```objc
- (CGRect) caretRectForPosition:(UITextPosition *) position;
```

#### Return Value

A rectangle that defines the area for drawing the caret.

#### Discussion

The system uses this value to calculate the length of the beam—the vertical line representing the pointer—when using a trackpad to interact with a text input area. You must implement this method even if text never becomes editable, and an insertion point caret never appears.

## Parameters

- `position`: An object that identifies a location in a text input area.

## See Also

### Related Documentation
- [func firstRect(for: UITextRange) -> CGRect](./firstrect%28for%29.md)
  Returns the first rectangle that encloses a range of text in a document.
- [UIPointerShape.verticalBeam(length:)](../uipointershape-swift.enum/verticalbeam%28length%29.md)
  The pointer morphs into a vertical beam using the specified length.
### Providing the caret layout information
- [func caretTransform(for: UITextPosition) -> CGAffineTransform](./carettransform%28for%29.md)
  Returns the transform to apply to the caret prior to drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/caretrect(for:))*