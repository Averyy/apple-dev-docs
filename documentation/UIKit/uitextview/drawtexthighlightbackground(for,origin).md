# drawTextHighlightBackground(for:origin:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func drawTextHighlightBackground(for textRange: NSTextRange, origin: CGPoint)
```

```objc
- (void) drawTextHighlightBackgroundForTextRange:(NSTextRange *) textRange origin:(CGPoint) origin;
```

## See Also

### Configuring appearance attributes
- [var font: UIFont?](./font.md)
  The font of the text.
- [var textColor: UIColor?](./textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]](./typingattributes.md)
  The attributes to apply to new text that the user enters.
- [var linkTextAttributes: [NSAttributedString.Key : Any]!](./linktextattributes.md)
  The attributes to apply to links.
- [var borderStyle: UITextView.BorderStyle](./borderstyle-swift.property.md)
  The border style for the text field.
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](./texthighlightattributes.md)
- [UITextView.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/drawtexthighlightbackground(for:origin:))*