# typingAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The attributes to apply to new text that the user enters.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var typingAttributes: [NSAttributedString.Key : Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,id> * typingAttributes;
```

## Discussion

This dictionary contains the attribute keys (and corresponding values) to apply to newly typed text. When the text field’s selection changes, the contents of the dictionary are cleared automatically.

If the text field is not in editing mode, this property contains the value `nil`. Similarly, you cannot assign a value to this property unless the text field is currently in editing mode.

## See Also

### Related Documentation
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the text field is currently in edit mode.
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
- [UITextField.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/typingattributes)*