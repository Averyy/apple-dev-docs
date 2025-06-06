# isLayoutMarginsRelativeArrangement

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isLayoutMarginsRelativeArrangement: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the stack view will layout its arranged views relative to its layout margins. If [`false`](https://developer.apple.com/documentation/swift/false), it lays out the arranged views relative to its bounds. The default is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var axis: NSLayoutConstraint.Axis](uistackview/axis.md)
  The axis along which the arranged views lay out.
- [var alignment: UIStackView.Alignment](uistackview/alignment-swift.property.md)
  The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [var distribution: UIStackView.Distribution](uistackview/distribution-swift.property.md)
  The distribution of the arranged views along the stack view’s axis.
- [var spacing: CGFloat](uistackview/spacing.md)
  The distance in points between the adjacent edges of the stack view’s arranged views.
- [var isBaselineRelativeArrangement: Bool](uistackview/isbaselinerelativearrangement.md)
  A Boolean value that determines whether the vertical spacing between views is measured from their baselines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/islayoutmarginsrelativearrangement)*