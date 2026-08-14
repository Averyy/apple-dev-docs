# UIStackView.Distribution.fill

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
case fill
```

#### Discussion

When the arranged views don’t fit within the stack view, it shrinks the views according to their compression resistance priority. If the arranged views don’t fill the stack view, it stretches the views according to their hugging priority. If there’s any ambiguity, the stack view resizes the arranged views based on their index in the [`arrangedSubviews`](uistackview/arrangedsubviews.md) array.

The following image shows an example of a horizontal stack view that uses the [`UIStackView.Distribution.fill`](uistackview/distribution-swift.enum/fill.md) distribution.

![A horizontal stack view with four arranged subviews. The stack view resizes the width of one of the arranged views so that it fills the available space along the stack view’s axis.](/images/com.apple.uikit/media-2557443@2x.png)

## See Also

- [UIStackView.Distribution.fillEqually](uistackview/distribution-swift.enum/fillequally.md)
  A layout where the stack view resizes all arranged views to the same size, filling the available space along the stack view’s axis.
- [UIStackView.Distribution.fillProportionally](uistackview/distribution-swift.enum/fillproportionally.md)
  A layout where the stack view resizes views proportionally based on their intrinsic content size to fill the available space along the stack view’s axis.
- [UIStackView.Distribution.equalSpacing](uistackview/distribution-swift.enum/equalspacing.md)
  A layout where the stack view maintains equal spacing between adjacent views while preserving their intrinsic content size.
- [UIStackView.Distribution.equalCentering](uistackview/distribution-swift.enum/equalcentering.md)
  A layout that attempts to position the arranged views with equal center-to-center spacing along the stack view’s axis, while maintaining the spacing property’s distance between views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/distribution-swift.enum/fill)*