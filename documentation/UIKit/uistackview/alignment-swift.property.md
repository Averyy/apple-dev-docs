# alignment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The alignment of the arranged subviews perpendicular to the stack view’s axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var alignment: UIStackView.Alignment { get set }
```

```objc
@property (nonatomic) UIStackViewAlignment alignment;
```

#### Discussion

This property determines how the stack view lays out its arranged views perpendicularly to its axis. The default value is [`UIStackView.Alignment.fill`](./alignment-swift.enum/fill.md). For a list of possible values, see [`UIStackView.Alignment`](./alignment-swift.enum.md).

## See Also

### Configuring the layout
- [var axis: NSLayoutConstraint.Axis](./axis.md)
  The axis along which the arranged views lay out.
- [var distribution: UIStackView.Distribution](./distribution-swift.property.md)
  The distribution of the arranged views along the stack view’s axis.
- [var spacing: CGFloat](./spacing.md)
  The distance in points between the adjacent edges of the stack view’s arranged views.
- [var isBaselineRelativeArrangement: Bool](./isbaselinerelativearrangement.md)
  A Boolean value that determines whether the vertical spacing between views is measured from their baselines.
- [var isLayoutMarginsRelativeArrangement: Bool](./islayoutmarginsrelativearrangement.md)
  A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/alignment-swift.property)*