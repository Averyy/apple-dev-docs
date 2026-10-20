# backgroundImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The custom background image for the tab bar.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var backgroundImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * backgroundImage;
```

#### Discussion

If you specify a stretchable background image, the tab bar stretches your image to fill the available space. If your image is not stretchable and not large enough to fill the available space, the tab bar tiles the image. For information about how stretching works, see the [`UIImage.ResizingMode`](../uiimage/resizingmode-swift.enum.md) type in [`UIImage`](../uiimage.md).

When a custom background image is present, the tab bar does not draw any blur effects behind itself, even when the [`isTranslucent`](./istranslucent.md) property is [`true`](../../Swift/true.md).

## See Also

### Changing the background
- [var barTintColor: UIColor?](./bartintcolor.md)
  The tint color to apply to the tab bar background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/backgroundimage)*