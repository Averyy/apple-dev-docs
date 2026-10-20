# rightView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The overlay view that displays on the right (or trailing) side of the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var rightView: UIView? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIView * rightView;
```

#### Discussion

You can use the right overlay view to provide indicate additional features available for the text field. For example, you might display a bookmarks button in this location to allow the user to select from a set of predefined items. The right overlay view flips automatically in a right-to-left user interface.

The right overlay view is placed in the rectangle returned by the [`rightViewRect(forBounds:)`](./rightviewrect%28forbounds%29.md) method of the receiver. The image associated with this property should fit the given rectangle. If it does not fit, it is scaled to fit. If you specify a control for your view, that control tracks and sends actions as usual.

If your right overlay view overlaps a sibling view, such as the clear button, you must use the [`UITextField.ViewMode`](./viewmode.md) to implement proper behavior. For example, if [`clearButtonMode`](./clearbuttonmode.md) is set to display the clear button, you can set the right overlay view’s [`rightViewMode`](./rightviewmode.md) to [`UITextField.ViewMode.unlessEditing`](./viewmode/unlessediting.md) to reveal the clear button during editing when the text field has contents.

## See Also

### Related Documentation
- [func rightViewRect(forBounds: CGRect) -> CGRect](./rightviewrect%28forbounds%29.md)
  Returns the drawing location of the text field’s right overlay view.
### Managing overlay views
- [var clearButtonMode: UITextField.ViewMode](./clearbuttonmode.md)
  A mode that controls when the standard Clear button appears in the text field.
- [var leftView: UIView?](./leftview.md)
  The overlay view that displays on the left (or leading) side of the text field.
- [var leftViewMode: UITextField.ViewMode](./leftviewmode.md)
  A mode that controls when the left overlay view appears in the text field.
- [var rightViewMode: UITextField.ViewMode](./rightviewmode.md)
  A mode that controls when the right overlay view appears in the text field.
- [UITextField.ViewMode](./viewmode.md)
  Constants that define when overlay views appear in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/rightview)*