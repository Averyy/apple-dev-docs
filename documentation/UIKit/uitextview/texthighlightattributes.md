# textHighlightAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var textHighlightAttributes: [NSAttributedString.Key : Any]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSDictionary<NSString *,id> * textHighlightAttributes;
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
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](./drawtexthighlightbackground%28for,origin%29.md)
- [UITextView.BorderStyle](./borderstyle-swift.enum.md)
  The type of border around the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/texthighlightattributes)*