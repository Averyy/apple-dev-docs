# layoutMarginsDidChange()

**Framework**: UIKit  
**Kind**: method

Notifies the view that the layout margins changed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func layoutMarginsDidChange()
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to respond when the value in the view’s [`layoutMargins`](uiview/layoutmargins.md) property changes. For example, you might override this method if your view subclass handles layout manually or uses the layout margins during drawing. In both cases, you could use this method to initiate a drawing or layout update.

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](uiview/directionallayoutmargins.md)
  The default spacing to use when laying out content in a view, taking into account the current language direction.
- [var layoutMargins: UIEdgeInsets](uiview/layoutmargins.md)
  The default spacing to use when laying out content in the view.
- [var preservesSuperviewLayoutMargins: Bool](uiview/preservessuperviewlayoutmargins.md)
  A Boolean value indicating whether the current view also respects the margins of its superview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layoutmarginsdidchange())*