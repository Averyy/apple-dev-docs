# UITextView.BorderStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The type of border around the text view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum BorderStyle
```

```c
enum UITextViewBorderStyle : NSInteger;
```

## Topics

### Enumeration Cases
- [UITextView.BorderStyle.none](./borderstyle-swift.enum/none.md)
  The text view does not display a border.
- [UITextView.BorderStyle.roundedRect](./borderstyle-swift.enum/roundedrect.md)
  Displays a rounded-style border for the text view.
### Initializers
- [init?(rawValue: Int)](./borderstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [func drawTextHighlightBackground(for: NSTextRange, origin: CGPoint)](./drawtexthighlightbackground%28for,origin%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/borderstyle-swift.enum)*