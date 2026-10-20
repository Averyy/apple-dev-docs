# attributedPlaceholder

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The styled string that displays when there is no other text in the text field.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var attributedPlaceholder: NSAttributedString? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedPlaceholder;
```

#### Discussion

This property is `nil` by default. If set, the placeholder string is drawn using system-defined color and the remaining style information (except the text color) of the attributed string. Assigning a new value to this property also replaces the value of the [`placeholder`](./placeholder.md) property with the same string data, albeit without any formatting information. Assigning a new value to this property does not affect any other style-related properties of the text field.

## See Also

### Configuring the text attributes
- [var text: String?](./text.md)
  The text that the text field displays.
- [var attributedText: NSAttributedString?](./attributedtext.md)
  The styled text that the text field displays.
- [var placeholder: String?](./placeholder.md)
  The string that displays when there is no other text in the text field.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/attributedplaceholder)*