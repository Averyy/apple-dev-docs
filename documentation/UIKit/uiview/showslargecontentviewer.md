# showsLargeContentViewer

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether to show the view in the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsLargeContentViewer: Bool { get set }
```

#### Discussion

For this property to take effect, the view must have a [`UILargeContentViewerInteraction`](uilargecontentviewerinteraction.md).

## See Also

- [var accessibilityIgnoresInvertColors: Bool](uiview/accessibilityignoresinvertcolors.md)
  A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [var largeContentImage: UIImage?](uiview/largecontentimage.md)
  An image that represents the view in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](uiview/largecontentimageinsets.md)
  Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [var largeContentTitle: String?](uiview/largecontenttitle.md)
  A string that describes the view in the large content viewer.
- [var scalesLargeContentImage: Bool](uiview/scaleslargecontentimage.md)
  A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/showslargecontentviewer)*