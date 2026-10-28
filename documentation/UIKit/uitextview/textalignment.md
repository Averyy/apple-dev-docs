# textAlignment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The technique for aligning the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var textAlignment: NSTextAlignment { get set }
```

```objc
@property (nonatomic) NSTextAlignment textAlignment;
```

## Discussion

This property applies to the entire text string. The default value of this property is [`NSTextAlignment.natural`](../nstextalignment/natural.md).

Assigning a new value to this property causes the new text alignment to be applied to the entire contents of the text view. If you want to apply the alignment to only a portion of the text, you must create a new attributed string with the desired style information and assign it to the [`attributedText`](./attributedtext.md) property.

## See Also

### Configuring appearance attributes
- [var font: UIFont?](./font.md)
  The font of the text.
- [var textColor: UIColor?](./textcolor.md)
  The color of the text.
- [var typingAttributes: [NSAttributedString.Key : Any]](./typingattributes.md)
  The attributes to apply to new text that the user enters.
- [var linkTextAttributes: [NSAttributedString.Key : Any]!](./linktextattributes.md)
  The attributes to apply to links.
- [var borderStyle: UITextView.BorderStyle](./borderstyle-swift.property.md)
  The border style for the text field.
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](./texthighlightattributes.md)
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](./drawtexthighlightbackground%28for,origin%29.md)
- [UITextView.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textalignment)*