# setContentCompressionResistancePriority(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the priority with which a view resists being made smaller than its intrinsic size.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setContentCompressionResistancePriority(_ priority: UILayoutPriority, for axis: NSLayoutConstraint.Axis)
```

```objc
- (void) setContentCompressionResistancePriority:(UILayoutPriority) priority forAxis:(UILayoutConstraintAxis) axis;
```

#### Discussion

Custom views should set default values for both orientations on creation, based on their content, typically to `UILayoutPriorityDefaultLow` or `UILayoutPriorityDefaultHigh`. When creating user interfaces, the layout designer can modify these priorities for specific views when the overall layout design requires different tradeoffs than the natural priorities of the views being used in the interface.

Subclasses should not override this method.

## Parameters

- `priority`: The new priority.
- `axis`: The axis for which the compression resistance priority should be set.

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
- [func contentHuggingPriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](./contenthuggingpriority%28for%29.md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](./setcontenthuggingpriority%28_,for%29.md)
  Sets the priority with which a view resists being made larger than its intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setcontentcompressionresistancepriority(_:for:))*