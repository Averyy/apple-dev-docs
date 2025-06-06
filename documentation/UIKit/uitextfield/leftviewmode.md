# leftViewMode

**Framework**: UIKit  
**Kind**: property

A mode that controls when the left overlay view appears in the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var leftViewMode: UITextField.ViewMode { get set }
```

#### Discussion

The default value for this property is [`UITextField.ViewMode.never`](uitextfield/viewmode/never.md). Note that the left overlay view flips automatically in a right-to-left user interface.

## See Also

- [var clearButtonMode: UITextField.ViewMode](uitextfield/clearbuttonmode.md)
  A mode that controls when the standard Clear button appears in the text field.
- [var leftView: UIView?](uitextfield/leftview.md)
  The overlay view that displays on the left (or leading) side of the text field.
- [var rightView: UIView?](uitextfield/rightview.md)
  The overlay view that displays on the right (or trailing) side of the text field.
- [var rightViewMode: UITextField.ViewMode](uitextfield/rightviewmode.md)
  A mode that controls when the right overlay view appears in the text field.
- [UITextField.ViewMode](uitextfield/viewmode.md)
  Constants that define when overlay views appear in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/leftviewmode)*