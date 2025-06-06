# backgroundImage

**Framework**: UIKit  
**Kind**: property

The custom background image for the tab bar.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backgroundImage: UIImage? { get set }
```

#### Discussion

If you specify a stretchable background image, the tab bar stretches your image to fill the available space. If your image is not stretchable and not large enough to fill the available space, the tab bar tiles the image. For information about how stretching works, see the [`UIImage.ResizingMode`](uiimage/resizingmode-swift.enum.md) type in [`UIImage`](uiimage.md).

When a custom background image is present, the tab bar does not draw any blur effects behind itself, even when the [`isTranslucent`](uitabbar/istranslucent.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var barTintColor: UIColor?](uitabbar/bartintcolor.md)
  The tint color to apply to the tab bar background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/backgroundimage)*