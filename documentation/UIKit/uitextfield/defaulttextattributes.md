# defaultTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The default attributes to apply to the text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var defaultTextAttributes: [NSAttributedString.Key : Any] { get set }
```

```objc
@property (nonatomic, copy) NSDictionary<NSString *,id> * defaultTextAttributes;
```

#### Discussion

By default, this property returns a dictionary of text attributes with default values.

Setting this property applies the specified attributes to the entire text of the text field. Unset attributes maintain their default values.

Getting this property returns the previously set attributes, which may have been modified by setting properties such as [`font`](./font.md) and [`textColor`](./textcolor.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/defaulttextattributes)*