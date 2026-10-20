# text

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text that the text field displays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var text: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * text;
```

#### Discussion

Assigning a new value to this property also replaces the value of the [`attributedText`](./attributedtext.md) property with the same text, albeit without any inherent style attributes. Instead the text view styles the new string using the [`font`](./font.md), [`textColor`](./textcolor.md), and other style-related properties of the class.

This value is `nil` by default.

## See Also

### Configuring the text attributes
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
- [UITextField.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/text)*