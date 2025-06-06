# drawText(in:)

**Framework**: UIKit  
**Kind**: method

Draws the text field’s text in the specified rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func drawText(in rect: CGRect)
```

#### Discussion

You should not call this method directly. If you want to customize the drawing behavior for the text, you can override this method to do your drawing.

By the time this method is called, the current graphics context is already configured with the default environment and text color for drawing. In your overridden method, you can configure the current context further and then invoke `super` to do the actual drawing or you can do the drawing yourself. If you do render the text yourself, you should not invoke `super`.

## Parameters

- `rect`: The rectangle in which to draw the text.

## See Also

- [func textRect(forBounds: CGRect) -> CGRect](uitextfield/textrect(forbounds:).md)
  Returns the drawing rectangle for the text field’s text.
- [func placeholderRect(forBounds: CGRect) -> CGRect](uitextfield/placeholderrect(forbounds:).md)
  Returns the drawing rectangle for the text field’s placeholder text.
- [func drawPlaceholder(in: CGRect)](uitextfield/drawplaceholder(in:).md)
  Draws the text field’s placeholder text in the specified rectangle.
- [func borderRect(forBounds: CGRect) -> CGRect](uitextfield/borderrect(forbounds:).md)
  Returns the text field’s border rectangle.
- [func editingRect(forBounds: CGRect) -> CGRect](uitextfield/editingrect(forbounds:).md)
  Returns the rectangle for displaying editable text.
- [func clearButtonRect(forBounds: CGRect) -> CGRect](uitextfield/clearbuttonrect(forbounds:).md)
  Returns the drawing rectangle for the built-in Clear button.
- [func leftViewRect(forBounds: CGRect) -> CGRect](uitextfield/leftviewrect(forbounds:).md)
  Returns the drawing rectangle of the text field’s left overlay view.
- [func rightViewRect(forBounds: CGRect) -> CGRect](uitextfield/rightviewrect(forbounds:).md)
  Returns the drawing location of the text field’s right overlay view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/drawtext(in:))*