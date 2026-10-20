# font

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The font of the printed text.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var font: UIFont? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIFont * font;
```

#### Discussion

If the value of this property is `nil` (the default), UIKit uses the standard system font, 12 points.

## See Also

### Text attributes for printed content
- [var color: UIColor?](./color.md)
  The color of the printed text.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The alignment of the printed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/font)*