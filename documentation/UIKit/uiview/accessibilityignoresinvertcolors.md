# accessibilityIgnoresInvertColors

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view ignores an accessibility request to invert its colors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var accessibilityIgnoresInvertColors: Bool { get set }
```

```objc
@property (nonatomic) BOOL accessibilityIgnoresInvertColors;
```

## Discussion

Inverting colors is often used to help users with light or color sensitivities to make bright colors darker. However, this behavior can have a destructive impact on images and videos. If inverting the colors would have a negative impact on your view’s content, set this property to [`true`](../../Swift/true.md) to prevent it from inverting its colors. Setting the property to [`true`](../../Swift/true.md) prevents the system from inverting the colors of the view and all of its subviews.

## See Also

### Modifying the accessibility behavior
- [var largeContentImage: UIImage?](./largecontentimage.md)
  An image that represents the view in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](./largecontentimageinsets.md)
  Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [var largeContentTitle: String?](./largecontenttitle.md)
  A string that describes the view in the large content viewer.
- [var scalesLargeContentImage: Bool](./scaleslargecontentimage.md)
  A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.
- [var showsLargeContentViewer: Bool](./showslargecontentviewer.md)
  A Boolean value that indicates whether to show the view in the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/accessibilityignoresinvertcolors)*