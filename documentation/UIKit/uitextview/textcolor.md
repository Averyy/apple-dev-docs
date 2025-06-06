# textColor

**Framework**: UIKit  
**Kind**: property

The color of the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textColor: UIColor? { get set }
```

#### Discussion

This property applies to the entire text string. The default text color is black.

In iOS 6 and later, assigning a new value to this property causes the new text color to be applied to the entire contents of the text view. If you want to apply the color to only a portion of the text, you must create a new attributed string with the desired style information and assign it to the [`attributedText`](uitextview/attributedtext.md) property.

## See Also

- [var backgroundColor: UIColor?](uiview/backgroundcolor.md)
  The view’s background color.
- [var font: UIFont?](uitextview/font.md)
  The font of the text.
- [var textAlignment: NSTextAlignment](uitextview/textalignment.md)
  The technique for aligning the text.
- [var typingAttributes: [NSAttributedString.Key : Any]](uitextview/typingattributes.md)
  The attributes to apply to new text that the user enters.
- [var linkTextAttributes: [NSAttributedString.Key : Any]!](uitextview/linktextattributes.md)
  The attributes to apply to links.
- [var borderStyle: UITextView.BorderStyle](uitextview/borderstyle-swift.property.md)
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](uitextview/texthighlightattributes.md)
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](uitextview/drawtexthighlightbackground(for:origin:).md)
- [UITextView.BorderStyle](uitextview/borderstyle-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textcolor)*