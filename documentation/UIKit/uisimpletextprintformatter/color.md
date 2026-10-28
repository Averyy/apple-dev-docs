# color

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color of the printed text.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var color: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * color;
```

## Discussion

If the value of this property is `nil` (the default), UIKit uses a black color when printing.

## See Also

### Text attributes for printed content
- [var font: UIFont?](./font.md)
  The font of the printed text.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The alignment of the printed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/color)*