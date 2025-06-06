# typingAttributes

**Framework**: UIKit  
**Kind**: property

The attributes to apply to new text that the user enters.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var typingAttributes: [NSAttributedString.Key : Any]? { get set }
```

#### Discussion

This dictionary contains the attribute keys (and corresponding values) to apply to newly typed text. When the text field’s selection changes, the contents of the dictionary are cleared automatically.

If the text field is not in editing mode, this property contains the value `nil`. Similarly, you cannot assign a value to this property unless the text field is currently in editing mode.

## See Also

- [var isEditing: Bool](uitextfield/isediting.md)
  A Boolean value that indicates whether the text field is currently in edit mode.
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
- [var textColor: UIColor?](uitextfield/textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](uitextfield/textalignment.md)
  The technique for aligning the text.
- [UITextField.BorderStyle](uitextfield/borderstyle-swift.enum.md)
  The type of border around the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/typingattributes)*