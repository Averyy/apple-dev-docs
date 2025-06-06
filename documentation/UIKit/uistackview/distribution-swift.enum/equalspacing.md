# UIStackView.Distribution.equalSpacing

**Framework**: UIKit  
**Kind**: case

A layout where the stack view positions its arranged views so that they fill the available space along the stack view’s axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case equalSpacing
```

#### Discussion

When the arranged views don’t fill the stack view, it pads the spacing between the views evenly. If the arranged views don’t fit within the stack view, it shrinks the views according to their compression resistance priority. If there’s any ambiguity, the stack view shrinks the views based on their index in the [`arrangedSubviews`](uistackview/arrangedsubviews.md) array.

The following image shows an example of a horizontal stack view that uses the [`UIStackView.Distribution.equalSpacing`](uistackview/distribution-swift.enum/equalspacing.md) distribution.

![A horizontal stack view with four arranged subviews. The stack view spaces the arranged views equally so that they fill the available space along the stack view’s axis.](https://docs-assets.developer.apple.com/published/04510fb208768aac2e839ee8c17db595/media-2557450%402x.png)

## See Also

- [UIStackView.Distribution.fill](uistackview/distribution-swift.enum/fill.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.fillEqually](uistackview/distribution-swift.enum/fillequally.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.fillProportionally](uistackview/distribution-swift.enum/fillproportionally.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.equalCentering](uistackview/distribution-swift.enum/equalcentering.md)
  A layout that attempts to position the arranged views with equal center-to-center spacing along the stack view’s axis, while maintaining the spacing property’s distance between views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/distribution-swift.enum/equalspacing)*