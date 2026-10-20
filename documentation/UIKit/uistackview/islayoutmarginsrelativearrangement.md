# isLayoutMarginsRelativeArrangement

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isLayoutMarginsRelativeArrangement: Bool { get set }
```

```objc
@property (nonatomic, getter=isLayoutMarginsRelativeArrangement) BOOL layoutMarginsRelativeArrangement;
```

#### Discussion

If [`true`](../../Swift/true.md), the stack view will layout its arranged views relative to its layout margins. If [`false`](../../Swift/false.md), it lays out the arranged views relative to its bounds. The default is [`false`](../../Swift/false.md).

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
- [var isBaselineRelativeArrangement: Bool](./isbaselinerelativearrangement.md)
  A Boolean value that determines whether the vertical spacing between views is measured from their baselines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/islayoutmarginsrelativearrangement)*