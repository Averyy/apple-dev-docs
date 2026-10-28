# largeContentImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An image that represents the view in the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var largeContentImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) UIImage * largeContentImage;
```

## Discussion

To present content in the large content viewer, you can provide either [`largeContentTitle`](./largecontenttitle.md) or [`largeContentImage`](./largecontentimage.md), or both.

This property defaults to an appropriate value for UIKit classes; otherwise, it’s `nil`.

## See Also

### Modifying the accessibility behavior
- [var accessibilityIgnoresInvertColors: Bool](./accessibilityignoresinvertcolors.md)
  A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [var largeContentImageInsets: UIEdgeInsets](./largecontentimageinsets.md)
  Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [var largeContentTitle: String?](./largecontenttitle.md)
  A string that describes the view in the large content viewer.
- [var scalesLargeContentImage: Bool](./scaleslargecontentimage.md)
  A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.
- [var showsLargeContentViewer: Bool](./showslargecontentviewer.md)
  A Boolean value that indicates whether to show the view in the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/largecontentimage)*