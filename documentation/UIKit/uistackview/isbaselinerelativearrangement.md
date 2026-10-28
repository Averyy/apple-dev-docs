# isBaselineRelativeArrangement

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the vertical spacing between views is measured from their baselines.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isBaselineRelativeArrangement: Bool { get set }
```

```objc
@property (nonatomic, getter=isBaselineRelativeArrangement) BOOL baselineRelativeArrangement;
```

## Discussion

If YES, the vertical space between views are measured from the last baseline of a text-based view, to the first baseline of the view below it. Top and bottom views are also positioned so that their closest baseline is the specified distance away from the stack view’s edge. This property is only used by vertical stack views. Use the [`alignment`](./alignment-swift.property.md) property to baseline align views in a horizontal stack view.

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the layout
- [var axis: NSLayoutConstraint.Axis](./axis.md)
  The axis along which the arranged views lay out.
- [var alignment: UIStackView.Alignment](./alignment-swift.property.md)
  The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [var distribution: UIStackView.Distribution](./distribution-swift.property.md)
  The distribution of the arranged views along the stack view’s axis.
- [var spacing: CGFloat](./spacing.md)
  The distance in points between the adjacent edges of the stack view’s arranged views.
- [var isLayoutMarginsRelativeArrangement: Bool](./islayoutmarginsrelativearrangement.md)
  A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/isbaselinerelativearrangement)*