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
var typingAttributes: [NSAttributedString.Key : Any] { get set }
```

```objc
@property (nonatomic, copy) NSDictionary<NSString *,id> * typingAttributes;
```

## Discussion

This dictionary contains the attribute keys (and corresponding values) to apply to newly typed text. When the text view’s selection changes, the contents of the dictionary are cleared automatically.

## See Also

### Related Documentation
- [var isEditable: Bool](./iseditable.md)
  A Boolean value that indicates whether the text view is editable.
### Configuring appearance attributes
- [var font: UIFont?](./font.md)
  The font of the text.
- [var textColor: UIColor?](./textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The technique for aligning the text.
- [var linkTextAttributes: [NSAttributedString.Key : Any]!](./linktextattributes.md)
  The attributes to apply to links.
- [var borderStyle: UITextView.BorderStyle](./borderstyle-swift.property.md)
  The border style for the text field.
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](./texthighlightattributes.md)
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](./drawtexthighlightbackground%28for,origin%29.md)
- [UITextView.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/typingattributes)*