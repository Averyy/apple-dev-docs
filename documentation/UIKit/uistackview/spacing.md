# spacing

**Framework**: UIKit  
**Kind**: property

The distance in points between the adjacent edges of the stack view’s arranged views.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var spacing: CGFloat { get set }
```

#### Discussion

This property defines a strict spacing between arranged views for the [`UIStackView.Distribution.fillProportionally`](uistackview/distribution-swift.enum/fillproportionally.md) distributions. It represents the minimum spacing for the [`UIStackView.Distribution.equalSpacing`](uistackview/distribution-swift.enum/equalspacing.md) and [`UIStackView.Distribution.equalCentering`](uistackview/distribution-swift.enum/equalcentering.md) distributions. Use negative values to allow overlap. The default value is `0.0`.

## See Also

- [var axis: NSLayoutConstraint.Axis](uistackview/axis.md)
  The axis along which the arranged views lay out.
- [var alignment: UIStackView.Alignment](uistackview/alignment-swift.property.md)
  The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [var distribution: UIStackView.Distribution](uistackview/distribution-swift.property.md)
  The distribution of the arranged views along the stack view’s axis.
- [var isBaselineRelativeArrangement: Bool](uistackview/isbaselinerelativearrangement.md)
  A Boolean value that determines whether the vertical spacing between views is measured from their baselines.
- [var isLayoutMarginsRelativeArrangement: Bool](uistackview/islayoutmarginsrelativearrangement.md)
  A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/spacing)*