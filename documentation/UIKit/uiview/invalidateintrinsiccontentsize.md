# invalidateIntrinsicContentSize()

**Framework**: UIKit  
**Kind**: method

Invalidates the view’s intrinsic content size.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func invalidateIntrinsicContentSize()
```

#### Discussion

Call this when something changes in your custom view that invalidates its intrinsic content size. This allows the constraint-based layout system to take the new intrinsic content size into account in its next layout pass.

## See Also

- [func systemLayoutSizeFitting(CGSize) -> CGSize](uiview/systemlayoutsizefitting(_:).md)
  Returns the optimal size of the view based on its current constraints.
- [func systemLayoutSizeFitting(CGSize, withHorizontalFittingPriority: UILayoutPriority, verticalFittingPriority: UILayoutPriority) -> CGSize](uiview/systemlayoutsizefitting(_:withhorizontalfittingpriority:verticalfittingpriority:).md)
  Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [var intrinsicContentSize: CGSize](uiview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](uiview/contentcompressionresistancepriority(for:).md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](uiview/setcontentcompressionresistancepriority(_:for:).md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](uiview/contenthuggingpriority(for:).md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](uiview/setcontenthuggingpriority(_:for:).md)
  Sets the priority with which a view resists being made larger than its intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/invalidateintrinsiccontentsize())*