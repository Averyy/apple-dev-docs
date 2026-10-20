# selectedImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The source image the item uses to generate its selected image.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var selectedImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * selectedImage;
```

#### Discussion

If `nil`, the item uses the value in [`image`](../uibaritem/image.md) instead. The item creates the images it displays from the alpha values in its source images. To prevent system tinting, use images with the [`UIImage.RenderingMode.alwaysOriginal`](../uiimage/renderingmode-swift.enum/alwaysoriginal.md) rendering mode. The item clips any image that’s larger than its bounds.

## See Also

### Configuring the item’s appearance
- [var standardAppearance: UITabBarAppearance?](./standardappearance.md)
  The appearance settings for a tab bar.
- [var scrollEdgeAppearance: UITabBarAppearance?](./scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var titlePositionAdjustment: UIOffset](./titlepositionadjustment.md)
  The offset to apply to the title’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/selectedimage)*