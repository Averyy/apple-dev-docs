# rightView

**Framework**: UIKit  
**Kind**: property

The overlay view that displays on the right (or trailing) side of the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var rightView: UIView? { get set }
```

#### Discussion

You can use the right overlay view to provide indicate additional features available for the text field. For example, you might display a bookmarks button in this location to allow the user to select from a set of predefined items. The right overlay view flips automatically in a right-to-left user interface.

The right overlay view is placed in the rectangle returned by the [`rightViewRect(forBounds:)`](uitextfield/rightviewrect(forbounds:).md) method of the receiver. The image associated with this property should fit the given rectangle. If it does not fit, it is scaled to fit. If you specify a control for your view, that control tracks and sends actions as usual.

If your right overlay view overlaps a sibling view, such as the clear button, you must use the [`UITextField.ViewMode`](uitextfield/viewmode.md) to implement proper behavior. For example, if [`clearButtonMode`](uitextfield/clearbuttonmode.md) is set to display the clear button, you can set the right overlay view’s [`rightViewMode`](uitextfield/rightviewmode.md) to [`UITextField.ViewMode.unlessEditing`](uitextfield/viewmode/unlessediting.md) to reveal the clear button during editing when the text field has contents.

## See Also

- [func rightViewRect(forBounds: CGRect) -> CGRect](uitextfield/rightviewrect(forbounds:).md)
  Returns the drawing location of the text field’s right overlay view.
- [var clearButtonMode: UITextField.ViewMode](uitextfield/clearbuttonmode.md)
  A mode that controls when the standard Clear button appears in the text field.
- [var leftView: UIView?](uitextfield/leftview.md)
  The overlay view that displays on the left (or leading) side of the text field.
- [var leftViewMode: UITextField.ViewMode](uitextfield/leftviewmode.md)
  A mode that controls when the left overlay view appears in the text field.
- [var rightViewMode: UITextField.ViewMode](uitextfield/rightviewmode.md)
  A mode that controls when the right overlay view appears in the text field.
- [UITextField.ViewMode](uitextfield/viewmode.md)
  Constants that define when overlay views appear in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/rightview)*