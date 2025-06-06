# linkTextAttributes

**Framework**: UIKit  
**Kind**: property

The attributes to apply to links.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var linkTextAttributes: [NSAttributedString.Key : Any]! { get set }
```

#### Discussion

The default attributes specify blue text with a single underline and the pointing hand cursor.

## See Also

- [var font: UIFont?](uitextview/font.md)
  The font of the text.
- [var textColor: UIColor?](uitextview/textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](uitextview/textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]](uitextview/typingattributes.md)
  The attributes to apply to new text that the user enters.
- [var borderStyle: UITextView.BorderStyle](uitextview/borderstyle-swift.property.md)
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](uitextview/texthighlightattributes.md)
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](uitextview/drawtexthighlightbackground(for:origin:).md)
- [UITextView.BorderStyle](uitextview/borderstyle-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/linktextattributes)*