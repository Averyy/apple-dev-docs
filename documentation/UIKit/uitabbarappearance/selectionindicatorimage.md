# selectionIndicatorImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image to draw for the selected item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var selectionIndicatorImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) UIImage * selectionIndicatorImage;
```

#### Discussion

UIKit renders the image in this property above the tab bar, but behind the tab bar item. If you specify a template or symbol image, UIKit renders that image with the tint color from the [`selectionIndicatorTintColor`](./selectionindicatortintcolor.md) property. If you specify any other type of image, UIKit displays your image without any additional tinting.

The default value of this property is `nil`, which causes UIKit to provide a default selection image.

## See Also

### Specifying the selection appearance
- [var selectionIndicatorTintColor: UIColor?](./selectionindicatortintcolor.md)
  The tint color to apply to the selection indicator image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarappearance/selectionindicatorimage)*