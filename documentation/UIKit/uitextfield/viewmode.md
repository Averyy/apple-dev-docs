# UITextField.ViewMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that define when overlay views appear in a text field.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum ViewMode
```

```c
enum UITextFieldViewMode : NSInteger;
```

## Topics

### Constants
- [UITextField.ViewMode.never](./viewmode/never.md)
  The overlay view never appears.
- [UITextField.ViewMode.whileEditing](./viewmode/whileediting.md)
  The overlay view is displayed only while text is being edited in the text field.
- [UITextField.ViewMode.unlessEditing](./viewmode/unlessediting.md)
  The overlay view is displayed only when text is not being edited.
- [UITextField.ViewMode.always](./viewmode/always.md)
  The overlay view is always displayed if the text field contains text.
### Initializers
- [init?(rawValue: Int)](./viewmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var rightViewMode: UITextField.ViewMode](./rightviewmode.md)
  A mode that controls when the right overlay view appears in the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/viewmode)*