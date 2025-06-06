# selectionIndicatorTintColor

**Framework**: UIKit  
**Kind**: property

The tint color to apply to the selection indicator image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var selectionIndicatorTintColor: UIColor? { get set }
```

#### Discussion

UIKit combines the color in this property with the image in the [`selectionIndicatorImage`](uitabbarappearance/selectionindicatorimage.md) to create the final appearance for the selected item. If you supplied a template image in [`selectionIndicatorImage`](uitabbarappearance/selectionindicatorimage.md), UIKit uses this color to tint that image. If [`selectionIndicatorImage`](uitabbarappearance/selectionindicatorimage.md) is `nil`, UIKit provides a default selection indicator image that accepts your tint color. If this property is `nil` or contains a clear color, UIKit doesn’t display a selection indicator.

If the image you supplied in [`selectionIndicatorImage`](uitabbarappearance/selectionindicatorimage.md) isn’t a template image, UIKit ignores the value in this property and displays your image as is.

The default value of this property is `nil`.

## See Also

- [var selectionIndicatorImage: UIImage?](uitabbarappearance/selectionindicatorimage.md)
  The image to draw for the selected item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarappearance/selectionindicatortintcolor)*