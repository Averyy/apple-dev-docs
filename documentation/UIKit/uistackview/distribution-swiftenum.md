# UIStackView.Distribution

**Framework**: UIKit  
**Kind**: enum

The layout that defines the size and position of the arranged views along the stack view’s axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum Distribution
```

## Topics

### Constants
- [UIStackView.Distribution.fill](uistackview/distribution-swift.enum/fill.md)
  A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackView.Distribution.fillEqually](uistackview/distribution-swift.enum/fillequally.md)
  A layout where the stack view resizes all arranged views to the same size, filling the available space along the stack view’s axis.
- [UIStackView.Distribution.fillProportionally](uistackview/distribution-swift.enum/fillproportionally.md)
  A layout where the stack view resizes views proportionally based on their intrinsic content size to fill the available space along the stack view’s axis.
- [UIStackView.Distribution.equalSpacing](uistackview/distribution-swift.enum/equalspacing.md)
  A layout where the stack view maintains equal spacing between adjacent views while preserving their intrinsic content size.
- [UIStackView.Distribution.equalCentering](uistackview/distribution-swift.enum/equalcentering.md)
  A layout that attempts to position the arranged views with equal center-to-center spacing along the stack view’s axis, while maintaining the spacing property’s distance between views.
### Initializers
- [init?(rawValue: Int)](uistackview/distribution-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [UIStackView.Alignment](uistackview/alignment-swift.enum.md)
  The layout of arranged views perpendicular to the stack view’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/distribution-swift.enum)*