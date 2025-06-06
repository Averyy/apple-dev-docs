# axis

**Framework**: UIKit  
**Kind**: property

The axis along which the arranged views lay out.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var axis: NSLayoutConstraint.Axis { get set }
```

#### Discussion

This property determines the orientation of the arranged views. Assigning the [`NSLayoutConstraint.Axis.vertical`](nslayoutconstraint/axis/vertical.md) value creates a column of views. Assigning the [`NSLayoutConstraint.Axis.horizontal`](nslayoutconstraint/axis/horizontal.md) value creates a row. The default value is [`NSLayoutConstraint.Axis.horizontal`](nslayoutconstraint/axis/horizontal.md).

## See Also

- [var alignment: UIStackView.Alignment](uistackview/alignment-swift.property.md)
  The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [var distribution: UIStackView.Distribution](uistackview/distribution-swift.property.md)
  The distribution of the arranged views along the stack view’s axis.
- [var spacing: CGFloat](uistackview/spacing.md)
  The distance in points between the adjacent edges of the stack view’s arranged views.
- [var isBaselineRelativeArrangement: Bool](uistackview/isbaselinerelativearrangement.md)
  A Boolean value that determines whether the vertical spacing between views is measured from their baselines.
- [var isLayoutMarginsRelativeArrangement: Bool](uistackview/islayoutmarginsrelativearrangement.md)
  A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/axis)*