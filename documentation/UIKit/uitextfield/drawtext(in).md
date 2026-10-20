# drawText(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Draws the text field’s text in the specified rectangle.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: The system no longer calls this method.

## Declaration

```swift
func drawText(in rect: CGRect)
```

```objc
- (void) drawTextInRect:(CGRect) rect;
```

#### Discussion

You should not call this method directly. If you want to customize the drawing behavior for the text, you can override this method to do your drawing.

By the time this method is called, the current graphics context is already configured with the default environment and text color for drawing. In your overridden method, you can configure the current context further and then invoke `super` to do the actual drawing or you can do the drawing yourself. If you do render the text yourself, you should not invoke `super`.

## Parameters

- `rect`: The rectangle in which to draw the text.

## See Also

### Drawing and positioning overrides
- [func textRect(forBounds: CGRect) -> CGRect](./textrect%28forbounds%29.md)
  Returns the drawing rectangle for the text field’s text.
- [func placeholderRect(forBounds: CGRect) -> CGRect](./placeholderrect%28forbounds%29.md)
  Returns the drawing rectangle for the text field’s placeholder text.
- [func drawPlaceholder(in: CGRect)](./drawplaceholder%28in%29.md)
  Draws the text field’s placeholder text in the specified rectangle.
- [func borderRect(forBounds: CGRect) -> CGRect](./borderrect%28forbounds%29.md)
  Returns the text field’s border rectangle.
- [func editingRect(forBounds: CGRect) -> CGRect](./editingrect%28forbounds%29.md)
  Returns the rectangle for displaying editable text.
- [func clearButtonRect(forBounds: CGRect) -> CGRect](./clearbuttonrect%28forbounds%29.md)
  Returns the drawing rectangle for the built-in Clear button.
- [func leftViewRect(forBounds: CGRect) -> CGRect](./leftviewrect%28forbounds%29.md)
  Returns the drawing rectangle of the text field’s left overlay view.
- [func rightViewRect(forBounds: CGRect) -> CGRect](./rightviewrect%28forbounds%29.md)
  Returns the drawing location of the text field’s right overlay view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/drawtext(in:))*