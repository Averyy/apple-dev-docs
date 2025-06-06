# UIStackView.Distribution.fillEqually

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
case fillEqually
```

#### Discussion

The views resize so that they’re all the same size along the stack view’s axis.

The following image shows an example of a horizontal stack view that uses the [`UIStackView.Distribution.fillEqually`](uistackview/distribution-swift.enum/fillequally.md) distribution.

![A horizontal stack view with four arranged subviews. The stack view resizes the width of the arranged views so that they fill the available space along the stack view’s axis, with each view having equal size.](https://docs-assets.developer.apple.com/published/1ed0432157959d227b0968a172a2651c/media-2557447%402x.png)

## See Also

- [UIStackView.Distribution.fill](uistackview/distribution-swift.enum/fill.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.fillProportionally](uistackview/distribution-swift.enum/fillproportionally.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.equalSpacing](uistackview/distribution-swift.enum/equalspacing.md)
  A layout where the stack view positions its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.equalCentering](uistackview/distribution-swift.enum/equalcentering.md)
  A layout that attempts to position the arranged views with equal center-to-center spacing along the stack view’s axis, while maintaining the spacing property’s distance between views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/distribution-swift.enum/fillequally)*