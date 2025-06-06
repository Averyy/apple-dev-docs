# text

**Framework**: UIKit  
**Kind**: property

The text that the text field displays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var text: String? { get set }
```

#### Discussion

Assigning a new value to this property also replaces the value of the [`attributedText`](uitextfield/attributedtext.md) property with the same text, albeit without any inherent style attributes. Instead the text view styles the new string using the [`font`](uitextfield/font.md), [`textColor`](uitextfield/textcolor.md), and other style-related properties of the class.

This value is `nil` by default.

## See Also

- [var attributedText: NSAttributedString?](uitextfield/attributedtext.md)
  The styled text that the text field displays.
- [var placeholder: String?](uitextfield/placeholder.md)
  The string that displays when there is no other text in the text field.
- [var attributedPlaceholder: NSAttributedString?](uitextfield/attributedplaceholder.md)
  The styled string that displays when there is no other text in the text field.
- [var defaultTextAttributes: [NSAttributedString.Key : Any]](uitextfield/defaulttextattributes.md)
  The default attributes to apply to the text.
- [var font: UIFont?](uitextfield/font.md)
  The font of the text.
- [var textColor: UIColor?](uitextfield/textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](uitextfield/textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]?](uitextfield/typingattributes.md)
  The attributes to apply to new text that the user enters.
- [UITextField.BorderStyle](uitextfield/borderstyle-swift.enum.md)
  The type of border around the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/text)*