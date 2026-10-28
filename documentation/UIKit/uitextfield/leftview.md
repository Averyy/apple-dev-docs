# leftView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The overlay view that displays on the left (or leading) side of the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var leftView: UIView? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIView * leftView;
```

## Discussion

You can use the left overlay view to indicate the intended behavior of the text field. For example, you might display a magnifying glass in this location to indicate that the text field is a search field. The left overlay view flips automatically in a right-to-left user interface.

The left overlay view is placed in the rectangle returned by the [`leftViewRect(forBounds:)`](./leftviewrect%28forbounds%29.md) method of the receiver. The image associated with this property should fit the given rectangle. If it does not fit, it is scaled to fit. If you specify a control for your view, the control tracks and sends actions as usual.

## See Also

### Related Documentation
- [func leftViewRect(forBounds: CGRect) -> CGRect](./leftviewrect%28forbounds%29.md)
  Returns the drawing rectangle of the text field’s left overlay view.
### Managing overlay views
- [var clearButtonMode: UITextField.ViewMode](./clearbuttonmode.md)
  A mode that controls when the standard Clear button appears in the text field.
- [var leftViewMode: UITextField.ViewMode](./leftviewmode.md)
  A mode that controls when the left overlay view appears in the text field.
- [var rightView: UIView?](./rightview.md)
  The overlay view that displays on the right (or trailing) side of the text field.
- [var rightViewMode: UITextField.ViewMode](./rightviewmode.md)
  A mode that controls when the right overlay view appears in the text field.
- [UITextField.ViewMode](./viewmode.md)
  Constants that define when overlay views appear in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/leftview)*