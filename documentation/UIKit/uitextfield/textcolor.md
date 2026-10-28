# textColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color of the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var textColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * textColor;
```

## Discussion

This property applies to the entire text string. The default value for this property is a black color. The value for the property can only be set to a non-`nil` value; setting this property to `nil` raises an exception.

If you are using styled text, assigning a new value to this property causes the text color to be applied to the entire string in the [`attributedText`](./attributedtext.md) property. If you want to apply the color to only a portion of the text, create a new attributed string with the desired style information and associate it with the text field.

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
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]?](./typingattributes.md)
  The attributes to apply to new text that the user enters.
- [UITextField.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/textcolor)*