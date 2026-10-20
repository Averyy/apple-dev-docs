# linkTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The attributes to apply to links.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var linkTextAttributes: [NSAttributedString.Key : Any]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSDictionary<NSString *,id> * linkTextAttributes;
```

#### Discussion

The default attributes specify blue text with a single underline and the pointing hand cursor.

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
- [var borderStyle: UITextView.BorderStyle](./borderstyle-swift.property.md)
  The border style for the text field.
- [var textHighlightAttributes: [NSAttributedString.Key : Any]!](./texthighlightattributes.md)
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](./drawtexthighlightbackground%28for,origin%29.md)
- [UITextView.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/linktextattributes)*