# contentHuggingPriority(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the priority with which a view resists being made larger than its intrinsic size.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func contentHuggingPriority(for axis: NSLayoutConstraint.Axis) -> UILayoutPriority
```

```objc
- (UILayoutPriority) contentHuggingPriorityForAxis:(UILayoutConstraintAxis) axis;
```

#### Return Value

The priority with which the view should resist being enlarged from its intrinsic size on the specified axis.

#### Discussion

The constraint-based layout system uses these priorities when determining the best layout for views that are encountering constraints that would require them to be larger than their intrinsic size.

## Parameters

- `axis`: The axis of the view that might be enlarged.

## See Also

### Measuring in Auto Layout
- [func systemLayoutSizeFitting(CGSize) -> CGSize](./systemlayoutsizefitting%28_%29.md)
  Returns the optimal size of the view based on its current constraints.
- [func systemLayoutSizeFitting(CGSize, withHorizontalFittingPriority: UILayoutPriority, verticalFittingPriority: UILayoutPriority) -> CGSize](./systemlayoutsizefitting%28_,withhorizontalfittingpriority,verticalfittingpriority%29.md)
  Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [var intrinsicContentSize: CGSize](./intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](./invalidateintrinsiccontentsize%28%29.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](./contentcompressionresistancepriority%28for%29.md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](./setcontentcompressionresistancepriority%28_,for%29.md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentHuggingPriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](./setcontenthuggingpriority%28_,for%29.md)
  Sets the priority with which a view resists being made larger than its intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/contenthuggingpriority(for:))*