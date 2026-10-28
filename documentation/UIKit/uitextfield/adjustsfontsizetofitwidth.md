# adjustsFontSizeToFitWidth

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to reduce the font size to fit the text string into the text field’s bounding rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var adjustsFontSizeToFitWidth: Bool { get set }
```

```objc
@property (nonatomic) BOOL adjustsFontSizeToFitWidth;
```

## Discussion

Normally, the text field’s content is drawn with the font you specify in the [`font`](./font.md) property. If this property is set to [`true`](../../Swift/true.md), however, and the contents in the [`text`](./text.md) property exceed the text field’s bounding rectangle, the receiver starts reducing the font size until the string fits or the minimum font size is reached. The text is shrunk along the baseline.

The default value for this property is [`false`](../../Swift/false.md). If you change it to [`true`](../../Swift/true.md), you should also set an appropriate minimum font size by modifying the [`minimumFontSize`](./minimumfontsize.md) property.

## See Also

### Sizing the text field’s text
- [var minimumFontSize: CGFloat](./minimumfontsize.md)
  The size of the smallest permissible font when drawing the text field’s text.
- [var sizingRule: UILetterformAwareSizingRule](../uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/adjustsfontsizetofitwidth)*