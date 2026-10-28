# attributedText

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The styled text that the text field displays.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var attributedText: NSAttributedString? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedText;
```

## Discussion

This property is `nil` by default. Assigning a new value to this property also replaces the value of the [`text`](./text.md) property with the same string data, albeit without any formatting information. In addition, assigning a new value updates the values in the [`font`](./font.md), [`textColor`](./textcolor.md), and other style-related properties so that they reflect the style information starting at location `0` in the attributed string.

## See Also

### Configuring the text attributes
- [var text: String?](./text.md)
  The text that the text field displays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/attributedtext)*