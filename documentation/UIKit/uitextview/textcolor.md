# textColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color of the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var textColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * textColor;
```

#### Discussion

This property applies to the entire text string. The default text color is black.

In iOS 6 and later, assigning a new value to this property causes the new text color to be applied to the entire contents of the text view. If you want to apply the color to only a portion of the text, you must create a new attributed string with the desired style information and assign it to the [`attributedText`](./attributedtext.md) property.

## See Also

### Related Documentation
- [var backgroundColor: UIColor?](../uiview/backgroundcolor.md)
  The view’s background color.
### Configuring appearance attributes
- [var font: UIFont?](./font.md)
  The font of the text.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The technique for aligning the text.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textcolor)*