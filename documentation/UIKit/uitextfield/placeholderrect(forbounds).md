# placeholderRect(forBounds:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the drawing rectangle for the text field’s placeholder text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func placeholderRect(forBounds bounds: CGRect) -> CGRect
```

```objc
- (CGRect) placeholderRectForBounds:(CGRect) bounds;
```

## Return Value

The computed drawing rectangle for the placeholder text.

## Discussion

You should not call this method directly. If you want to customize the drawing rectangle for the placeholder text, you can override this method and return a different rectangle.

If the placeholder string is empty or `nil`, this method is not called.

## Parameters

- `bounds`: The bounding rectangle of the receiver.

## See Also

### Drawing and positioning overrides
- [func textRect(forBounds: CGRect) -> CGRect](./textrect%28forbounds%29.md)
  Returns the drawing rectangle for the text field’s text.
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
- [func drawText(in: CGRect)](./drawtext%28in%29.md)
  Draws the text field’s text in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/placeholderrect(forbounds:))*