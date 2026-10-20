# UITextField.BorderStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The type of border around the text field.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum BorderStyle
```

```c
enum UITextBorderStyle : NSInteger;
```

## Topics

### Constants
- [UITextField.BorderStyle.none](./borderstyle-swift.enum/none.md)
  The text field does not display a border.
- [UITextField.BorderStyle.line](./borderstyle-swift.enum/line.md)
  Displays a thin rectangle around the text field.
- [UITextField.BorderStyle.bezel](./borderstyle-swift.enum/bezel.md)
  Displays a bezel-style border for the text field. This style is typically used for standard data-entry fields.
- [UITextField.BorderStyle.roundedRect](./borderstyle-swift.enum/roundedrect.md)
  Displays a rounded-style border for the text field.
### Initializers
- [init?(rawValue: Int)](./borderstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the text attributes
- [var text: String?](./text.md)
  The text that the text field displays.
- [var attributedText: NSAttributedString?](./attributedtext.md)
  The styled text that the text field displays.
- [var placeholder: String?](./placeholder.md)
  The string that displays when there is no other text in the text field.
- [var attributedPlaceholder: NSAttributedString?](./attributedplaceholder.md)
  The styled string that displays when there is no other text in the text field.
- [var defaultTextAttributes: [NSAttributedString.Key : Any]](./defaulttextattributes.md)
  The default attributes to apply to the text.
- [var font: UIFont?](./font.md)
  The font of the text.
- [var textColor: UIColor?](./textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]?](./typingattributes.md)
  The attributes to apply to new text that the user enters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/borderstyle-swift.enum)*