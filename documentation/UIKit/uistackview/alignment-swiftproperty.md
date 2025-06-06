# alignment

**Framework**: UIKit  
**Kind**: property

The alignment of the arranged subviews perpendicular to the stack view’s axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var alignment: UIStackView.Alignment { get set }
```

#### Discussion

This property determines how the stack view lays out its arranged views perpendicularly to its axis. The default value is [`UIStackView.Alignment.fill`](uistackview/alignment-swift.enum/fill.md). For a list of possible values, see [`UIStackView.Alignment`](uistackview/alignment-swift.enum.md).

## See Also

- [var axis: NSLayoutConstraint.Axis](uistackview/axis.md)
  The axis along which the arranged views lay out.
- [var distribution: UIStackView.Distribution](uistackview/distribution-swift.property.md)
  The distribution of the arranged views along the stack view’s axis.
- [var spacing: CGFloat](uistackview/spacing.md)
  The distance in points between the adjacent edges of the stack view’s arranged views.
- [var isBaselineRelativeArrangement: Bool](uistackview/isbaselinerelativearrangement.md)
  A Boolean value that determines whether the vertical spacing between views is measured from their baselines.
- [var isLayoutMarginsRelativeArrangement: Bool](uistackview/islayoutmarginsrelativearrangement.md)
  A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/alignment-swift.property)*