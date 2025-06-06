# attributedText

**Framework**: UIKit  
**Kind**: property

The styled text that the text field displays.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var attributedText: NSAttributedString? { get set }
```

#### Discussion

This property is `nil` by default. Assigning a new value to this property also replaces the value of the [`text`](uitextfield/text.md) property with the same string data, albeit without any formatting information. In addition, assigning a new value updates the values in the [`font`](uitextfield/font.md), [`textColor`](uitextfield/textcolor.md), and other style-related properties so that they reflect the style information starting at location `0` in the attributed string.

## See Also

- [var text: String?](uitextfield/text.md)
  The text that the text field displays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/attributedtext)*