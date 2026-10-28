# font

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The font of the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var font: UIFont? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIFont * font;
```

## Discussion

This property applies to the entire text of the text field. It also applies to the placeholder text. The default value of this property is the body style of the system font.

Assigning a new value to this property causes the font to be applied to the entire string in the [`attributedText`](./attributedtext.md) and [`attributedPlaceholder`](./attributedplaceholder.md) properties. If you want to apply the font to only a portion of the text, create a new attributed string with the desired style information and associate it with the text field.

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
- [var textColor: UIColor?](./textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]?](./typingattributes.md)
  The attributes to apply to new text that the user enters.
- [UITextField.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/font)*