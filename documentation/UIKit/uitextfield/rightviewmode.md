# rightViewMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A mode that controls when the right overlay view appears in the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var rightViewMode: UITextField.ViewMode { get set }
```

```objc
@property (nonatomic) UITextFieldViewMode rightViewMode;
```

#### Discussion

The default value for this property is [`UITextField.ViewMode.never`](./viewmode/never.md). Note that the right overlay view flips automatically in a right-to-left user interface.

## See Also

### Managing overlay views
- [var clearButtonMode: UITextField.ViewMode](./clearbuttonmode.md)
  A mode that controls when the standard Clear button appears in the text field.
- [var leftView: UIView?](./leftview.md)
  The overlay view that displays on the left (or leading) side of the text field.
- [var leftViewMode: UITextField.ViewMode](./leftviewmode.md)
  A mode that controls when the left overlay view appears in the text field.
- [var rightView: UIView?](./rightview.md)
  The overlay view that displays on the right (or trailing) side of the text field.
- [UITextField.ViewMode](./viewmode.md)
  Constants that define when overlay views appear in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/rightviewmode)*