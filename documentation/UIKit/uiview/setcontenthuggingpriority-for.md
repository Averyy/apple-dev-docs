# setContentHuggingPriority(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the priority with which a view resists being made larger than its intrinsic size.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setContentHuggingPriority(_ priority: UILayoutPriority, for axis: NSLayoutConstraint.Axis)
```

#### Discussion

Custom views should set default values for both orientations on creation, based on their content, typically to `UILayoutPriorityDefaultLow` or `UILayoutPriorityDefaultHigh`. When creating user interfaces, the layout designer can modify these priorities for specific views when the overall layout design requires different tradeoffs than the natural priorities of the views being used in the interface.

Subclasses should not override this method.

## Parameters

- `priority`: The new priority.
- `axis`: The axis for which the content hugging priority should be set.

## See Also

- [func systemLayoutSizeFitting(CGSize) -> CGSize](uiview/systemlayoutsizefitting(_:).md)
  Returns the optimal size of the view based on its current constraints.
- [func systemLayoutSizeFitting(CGSize, withHorizontalFittingPriority: UILayoutPriority, verticalFittingPriority: UILayoutPriority) -> CGSize](uiview/systemlayoutsizefitting(_:withhorizontalfittingpriority:verticalfittingpriority:).md)
  Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [var intrinsicContentSize: CGSize](uiview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](uiview/invalidateintrinsiccontentsize.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](uiview/contentcompressionresistancepriority(for:).md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](uiview/setcontentcompressionresistancepriority(_:for:).md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](uiview/contenthuggingpriority(for:).md)
  Returns the priority with which a view resists being made larger than its intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setcontenthuggingpriority(_:for:))*