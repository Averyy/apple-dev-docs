# isBaselineRelativeArrangement

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the vertical spacing between views is measured from their baselines.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isBaselineRelativeArrangement: Bool { get set }
```

#### Discussion

If YES, the vertical space between views are measured from the last baseline of a text-based view, to the first baseline of the view below it. Top and bottom views are also positioned so that their closest baseline is the specified distance away from the stack view’s edge. This property is only used by vertical stack views. Use the [`alignment`](uistackview/alignment-swift.property.md) property to baseline align views in a horizontal stack view.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var axis: NSLayoutConstraint.Axis](uistackview/axis.md)
  The axis along which the arranged views lay out.
- [var alignment: UIStackView.Alignment](uistackview/alignment-swift.property.md)
  The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [var distribution: UIStackView.Distribution](uistackview/distribution-swift.property.md)
  The distribution of the arranged views along the stack view’s axis.
- [var spacing: CGFloat](uistackview/spacing.md)
  The distance in points between the adjacent edges of the stack view’s arranged views.
- [var isLayoutMarginsRelativeArrangement: Bool](uistackview/islayoutmarginsrelativearrangement.md)
  A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/isbaselinerelativearrangement)*