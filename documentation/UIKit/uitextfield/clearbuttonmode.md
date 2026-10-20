# clearButtonMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A mode that controls when the standard Clear button appears in the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var clearButtonMode: UITextField.ViewMode { get set }
```

```objc
@property (nonatomic) UITextFieldViewMode clearButtonMode;
```

#### Discussion

The standard clear button displays at the right side of the text field when the text field has contents, providing a way for the user to remove text quickly.

This button appears automatically based on the value of this property. The default value for this property is [`UITextField.ViewMode.never`](./viewmode/never.md).

## See Also

### Managing overlay views
- [var leftView: UIView?](./leftview.md)
  The overlay view that displays on the left (or leading) side of the text field.
- [var leftViewMode: UITextField.ViewMode](./leftviewmode.md)
  A mode that controls when the left overlay view appears in the text field.
- [var rightView: UIView?](./rightview.md)
  The overlay view that displays on the right (or trailing) side of the text field.
- [var rightViewMode: UITextField.ViewMode](./rightviewmode.md)
  A mode that controls when the right overlay view appears in the text field.
- [UITextField.ViewMode](./viewmode.md)
  Constants that define when overlay views appear in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/clearbuttonmode)*