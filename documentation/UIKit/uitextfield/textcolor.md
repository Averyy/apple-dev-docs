# textColor

**Framework**: UIKit  
**Kind**: property

The color of the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textColor: UIColor? { get set }
```

#### Discussion

This property applies to the entire text string. The default value for this property is a black color. The value for the property can only be set to a non-`nil` value; setting this property to `nil` raises an exception.

If you are using styled text, assigning a new value to this property causes the text color to be applied to the entire string in the [`attributedText`](uitextfield/attributedtext.md) property. If you want to apply the color to only a portion of the text, create a new attributed string with the desired style information and associate it with the text field.

## See Also

- [var text: String?](uitextfield/text.md)
  The text that the text field displays.
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
- [var textAlignment: NSTextAlignment](uitextfield/textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]?](uitextfield/typingattributes.md)
  The attributes to apply to new text that the user enters.
- [UITextField.BorderStyle](uitextfield/borderstyle-swift.enum.md)
  The type of border around the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/textcolor)*