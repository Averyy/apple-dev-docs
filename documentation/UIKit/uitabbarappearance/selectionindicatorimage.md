# selectionIndicatorImage

**Framework**: UIKit  
**Kind**: property

The image to draw for the selected item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectionIndicatorImage: UIImage? { get set }
```

#### Discussion

UIKit renders the image in this property above the tab bar, but behind the tab bar item. If you specify a template or symbol image, UIKit renders that image with the tint color from the [`selectionIndicatorTintColor`](uitabbarappearance/selectionindicatortintcolor.md) property. If you specify any other type of image, UIKit displays your image without any additional tinting.

The default value of this property is `nil`, which causes UIKit to provide a default selection image.

## See Also

- [var selectionIndicatorTintColor: UIColor?](uitabbarappearance/selectionindicatortintcolor.md)
  The tint color to apply to the selection indicator image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarappearance/selectionindicatorimage)*