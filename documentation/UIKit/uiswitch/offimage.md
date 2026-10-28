# offImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image displayed when the switch is in the off position.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var offImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * offImage;
```

## Discussion

In iOS 7 and later, this property has no effect.

In iOS 6, this image represents the interior contents of the switch. The image you specify is composited with the switch’s rounded bezel and thumb to create the final appearance.

## See Also

### Deprecated
- [var onImage: UIImage?](./onimage.md)
  The image displayed when the switch is in the on position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/offimage)*