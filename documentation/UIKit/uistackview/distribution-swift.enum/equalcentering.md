# UIStackView.Distribution.equalCentering

**Framework**: UIKit  
**Kind**: case

A layout that attempts to position the arranged views with equal center-to-center spacing along the stack view’s axis, while maintaining the spacing property’s distance between views.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case equalCentering
```

#### Discussion

If the arranged views don’t fit within the stack view, it shrinks the spacing until it reaches the minimum spacing defined by its [`spacing`](uistackview/spacing.md) property. If the views still don’t fit, the stack view shrinks the arranged views according to their compression resistance priority. If there’s any ambiguity, the stack view shrinks the views based on their index in the [`arrangedSubviews`](uistackview/arrangedsubviews.md) array.

The following image shows an example of a horizontal stack view that uses the [`UIStackView.Distribution.equalSpacing`](uistackview/distribution-swift.enum/equalspacing.md) distribution.

![A horizontal stack view with four arranged subviews. The stack view spaces the arranged views with equal center-to-center spacing along the stack view’s axis.](https://docs-assets.developer.apple.com/published/bc4851ca81324cf9b29c51c98131d69e/media-2557452%402x.png)

> **Note**:  The stack view maintains the intrinsic content size of its arranged views at the expense of the center-to-center spacing. Similarly, it maintains the minimum spacing between views at the expense of the view’s intrinsic content size.

 The stack view maintains the intrinsic content size of its arranged views at the expense of the center-to-center spacing. Similarly, it maintains the minimum spacing between views at the expense of the view’s intrinsic content size.

## See Also

- [UIStackView.Distribution.fill](uistackview/distribution-swift.enum/fill.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.fillEqually](uistackview/distribution-swift.enum/fillequally.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.fillProportionally](uistackview/distribution-swift.enum/fillproportionally.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.equalSpacing](uistackview/distribution-swift.enum/equalspacing.md)
  A layout where the stack view positions its arranged views so that they fill the available space along the stack view’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/distribution-swift.enum/equalcentering)*