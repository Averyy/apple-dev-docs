# intrinsicContentSize

**Framework**: UIKit  
**Kind**: property

The natural size for the receiving view, considering only properties of the view itself.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var intrinsicContentSize: CGSize { get }
```

#### Discussion

Custom views typically have content that they display of which the layout system is unaware. Setting this property allows a custom view to communicate to the layout system what size it would like to be based on its content. This intrinsic size must be independent of the content frame, because there’s no way to dynamically communicate a changed width to the layout system based on a changed height, for example.

If a custom view has no intrinsic size for a given dimension, it can use [`noIntrinsicMetric`](uiview/nointrinsicmetric.md) for that dimension.

## See Also

- [func systemLayoutSizeFitting(CGSize) -> CGSize](uiview/systemlayoutsizefitting(_:).md)
  Returns the optimal size of the view based on its current constraints.
- [func systemLayoutSizeFitting(CGSize, withHorizontalFittingPriority: UILayoutPriority, verticalFittingPriority: UILayoutPriority) -> CGSize](uiview/systemlayoutsizefitting(_:withhorizontalfittingpriority:verticalfittingpriority:).md)
  Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [func invalidateIntrinsicContentSize()](uiview/invalidateintrinsiccontentsize.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](uiview/contentcompressionresistancepriority(for:).md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](uiview/setcontentcompressionresistancepriority(_:for:).md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](uiview/contenthuggingpriority(for:).md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](uiview/setcontenthuggingpriority(_:for:).md)
  Sets the priority with which a view resists being made larger than its intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/intrinsiccontentsize)*