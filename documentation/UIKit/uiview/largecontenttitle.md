# largeContentTitle

**Framework**: UIKit  
**Kind**: property

A string that describes the view in the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var largeContentTitle: String? { get set }
```

#### Discussion

To present content in the large content viewer, you can provide either [`largeContentTitle`](uilargecontentvieweritem/largecontenttitle.md) or [`largeContentImage`](uilargecontentvieweritem/largecontentimage.md), or both.

This property defaults to an appropriate value for UIKit classes; otherwise, it’s `nil`.

## See Also

- [var accessibilityIgnoresInvertColors: Bool](uiview/accessibilityignoresinvertcolors.md)
  A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [var largeContentImage: UIImage?](uiview/largecontentimage.md)
  An image that represents the view in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](uiview/largecontentimageinsets.md)
  Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [var scalesLargeContentImage: Bool](uiview/scaleslargecontentimage.md)
  A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.
- [var showsLargeContentViewer: Bool](uiview/showslargecontentviewer.md)
  A Boolean value that indicates whether to show the view in the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/largecontenttitle)*