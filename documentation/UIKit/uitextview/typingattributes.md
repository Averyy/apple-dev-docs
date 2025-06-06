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
var typingAttributes: [NSAttributedString.Key : Any] { get set }
```

#### Discussion

This dictionary contains the attribute keys (and corresponding values) to apply to newly typed text. When the text view’s selection changes, the contents of the dictionary are cleared automatically.

## See Also

- [var isEditable: Bool](uitextview/iseditable.md)
  A Boolean value that indicates whether the text view is editable.
- [var font: UIFont?](uitextview/font.md)
  The font of the text.
- [var textColor: UIColor?](uitextview/textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](uitextview/textalignment.md)
  The technique for aligning the text.
- [var linkTextAttributes: [NSAttributedString.Key : Any]!](uitextview/linktextattributes.md)
  The attributes to apply to links.
- [var borderStyle: UITextView.BorderStyle](uitextview/borderstyle-swift.property.md)
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](uitextview/texthighlightattributes.md)
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](uitextview/drawtexthighlightbackground(for:origin:).md)
- [UITextView.BorderStyle](uitextview/borderstyle-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/typingattributes)*