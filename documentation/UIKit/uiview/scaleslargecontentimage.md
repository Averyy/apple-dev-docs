# scalesLargeContentImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var scalesLargeContentImage: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL scalesLargeContentImage;
```

#### Discussion

If [`false`](../../Swift/false.md), the viewer displays the image at its intrinsic size.

> 💡 **Tip**:  For best results when scaling, use a PDF asset and select the Preserve Vector Data option in the asset catalog.

## See Also

### Modifying the accessibility behavior
- [var accessibilityIgnoresInvertColors: Bool](./accessibilityignoresinvertcolors.md)
  A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [var largeContentImage: UIImage?](./largecontentimage.md)
  An image that represents the view in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](./largecontentimageinsets.md)
  Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [var largeContentTitle: String?](./largecontenttitle.md)
  A string that describes the view in the large content viewer.
- [var showsLargeContentViewer: Bool](./showslargecontentviewer.md)
  A Boolean value that indicates whether to show the view in the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/scaleslargecontentimage)*