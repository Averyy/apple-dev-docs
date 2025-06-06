# editingRect(forBounds:)

**Framework**: UIKit  
**Kind**: method

Returns the rectangle for displaying editable text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func editingRect(forBounds bounds: CGRect) -> CGRect
```

#### Return Value

The computed editing rectangle for the text.

#### Discussion

You should not call this method directly. If you want to provide a different editing rectangle for the text, you can override this method and return that rectangle. By default, this method returns a region in the text field that is not occupied by any overlay views.

## Parameters

- `bounds`: The bounding rectangle of the receiver.

## See Also

- [func textRect(forBounds: CGRect) -> CGRect](uitextfield/textrect(forbounds:).md)
  Returns the drawing rectangle for the text field’s text.
- [func drawText(in: CGRect)](uitextfield/drawtext(in:).md)
  Draws the text field’s text in the specified rectangle.
- [func placeholderRect(forBounds: CGRect) -> CGRect](uitextfield/placeholderrect(forbounds:).md)
  Returns the drawing rectangle for the text field’s placeholder text.
- [func drawPlaceholder(in: CGRect)](uitextfield/drawplaceholder(in:).md)
  Draws the text field’s placeholder text in the specified rectangle.
- [func borderRect(forBounds: CGRect) -> CGRect](uitextfield/borderrect(forbounds:).md)
  Returns the text field’s border rectangle.
- [func clearButtonRect(forBounds: CGRect) -> CGRect](uitextfield/clearbuttonrect(forbounds:).md)
  Returns the drawing rectangle for the built-in Clear button.
- [func leftViewRect(forBounds: CGRect) -> CGRect](uitextfield/leftviewrect(forbounds:).md)
  Returns the drawing rectangle of the text field’s left overlay view.
- [func rightViewRect(forBounds: CGRect) -> CGRect](uitextfield/rightviewrect(forbounds:).md)
  Returns the drawing location of the text field’s right overlay view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/editingrect(forbounds:))*