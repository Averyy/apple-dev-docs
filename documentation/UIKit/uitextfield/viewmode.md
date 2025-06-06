# UITextField.ViewMode

**Framework**: UIKit  
**Kind**: enum

Constants that define when overlay views appear in a text field.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum ViewMode
```

## Topics

### Constants
- [UITextField.ViewMode.never](uitextfield/viewmode/never.md)
  The overlay view never appears.
- [UITextField.ViewMode.whileEditing](uitextfield/viewmode/whileediting.md)
  The overlay view is displayed only while text is being edited in the text field.
- [UITextField.ViewMode.unlessEditing](uitextfield/viewmode/unlessediting.md)
  The overlay view is displayed only when text is not being edited.
- [UITextField.ViewMode.always](uitextfield/viewmode/always.md)
  The overlay view is always displayed if the text field contains text.
### Initializers
- [init?(rawValue: Int)](uitextfield/viewmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var clearButtonMode: UITextField.ViewMode](uitextfield/clearbuttonmode.md)
  A mode that controls when the standard Clear button appears in the text field.
- [var leftView: UIView?](uitextfield/leftview.md)
  The overlay view that displays on the left (or leading) side of the text field.
- [var leftViewMode: UITextField.ViewMode](uitextfield/leftviewmode.md)
  A mode that controls when the left overlay view appears in the text field.
- [var rightView: UIView?](uitextfield/rightview.md)
  The overlay view that displays on the right (or trailing) side of the text field.
- [var rightViewMode: UITextField.ViewMode](uitextfield/rightviewmode.md)
  A mode that controls when the right overlay view appears in the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/viewmode)*