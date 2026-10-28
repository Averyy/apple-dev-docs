# clearButtonRect(forBounds:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the drawing rectangle for the built-in Clear button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func clearButtonRect(forBounds bounds: CGRect) -> CGRect
```

```objc
- (CGRect) clearButtonRectForBounds:(CGRect) bounds;
```

## Return Value

The rectangle in which to draw the clear button.

## Discussion

You should not call this method directly. If you want to place the clear button in a different location, you can override this method and return the new rectangle. Your method should call the `super` implementation and modify the returned rectangle’s origin only. Changing the size of the clear button may cause unnecessary distortion of the button image.

## Parameters

- `bounds`: The bounding rectangle of the receiver.

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
- [func leftViewRect(forBounds: CGRect) -> CGRect](./leftviewrect%28forbounds%29.md)
  Returns the drawing rectangle of the text field’s left overlay view.
- [func rightViewRect(forBounds: CGRect) -> CGRect](./rightviewrect%28forbounds%29.md)
  Returns the drawing location of the text field’s right overlay view.
- [func drawText(in: CGRect)](./drawtext%28in%29.md)
  Draws the text field’s text in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/clearbuttonrect(forbounds:))*