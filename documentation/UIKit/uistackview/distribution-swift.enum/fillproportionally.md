# UIStackView.Distribution.fillProportionally

**Framework**: UIKit  
**Kind**: case

A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case fillProportionally
```

#### Discussion

The views resize proportionally according to their intrinsic content size along the stack view’s axis.

The following image shows an example of a horizontal stack view that uses the [`UIStackView.Distribution.fillProportionally`](uistackview/distribution-swift.enum/fillproportionally.md) distribution.

![A horizontal stack view with four arranged subviews. The stack view resizes the width of the arranged views so that they fill the available space along the stack view’s axis, with the views varying in size.](https://docs-assets.developer.apple.com/published/556a89349bbaf33d5677b22d6ec262ac/media-2557449%402x.png)

## See Also

- [UIStackView.Distribution.fill](uistackview/distribution-swift.enum/fill.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.fillEqually](uistackview/distribution-swift.enum/fillequally.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.equalSpacing](uistackview/distribution-swift.enum/equalspacing.md)
  A layout where the stack view positions its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.equalCentering](uistackview/distribution-swift.enum/equalcentering.md)
  A layout that attempts to position the arranged views with equal center-to-center spacing along the stack view’s axis, while maintaining the spacing property’s distance between views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/distribution-swift.enum/fillproportionally)*