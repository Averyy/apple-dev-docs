# scalesLargeContentImage

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var scalesLargeContentImage: Bool { get set }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/swift/false), the viewer displays the image at its intrinsic size.

> 💡 **Tip**:  For best results when scaling, use a PDF asset and select the Preserve Vector Data option in the asset catalog.

## See Also

- [var accessibilityIgnoresInvertColors: Bool](uiview/accessibilityignoresinvertcolors.md)
  A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [var largeContentImage: UIImage?](uiview/largecontentimage.md)
  An image that represents the view in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](uiview/largecontentimageinsets.md)
  Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [var largeContentTitle: String?](uiview/largecontenttitle.md)
  A string that describes the view in the large content viewer.
- [var showsLargeContentViewer: Bool](uiview/showslargecontentviewer.md)
  A Boolean value that indicates whether to show the view in the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/scaleslargecontentimage)*