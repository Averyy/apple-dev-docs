# layoutMargins

**Framework**: UIKit  
**Kind**: property

The default spacing to use when laying out content in the view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var layoutMargins: UIEdgeInsets { get set }
```

#### Discussion

In iOS 11 and later, use the [`directionalLayoutMargins`](uiview/directionallayoutmargins.md) property to specify layout margins instead of this property. The leading and trailing edge insets in the [`directionalLayoutMargins`](uiview/directionallayoutmargins.md) property are synchronized with the left and right insets in this property. For example, setting the [`leading`](nsdirectionaledgeinsets/leading.md) directional edge inset to 20 points causes the [`left`](uiedgeinsets/left.md) inset of this property to be set to 20 points on a system with a left-to-right language.

For the root view of a view controller, the default value of this property reflects the system minimum margins and safe area insets. For other subviews in your view hierarchy, the default layout margins are normally 8 points on each side, but the values may be greater if the view is not fully inside the safe area or if the [`preservesSuperviewLayoutMargins`](uiview/preservessuperviewlayoutmargins.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).

This property specifies the desired amount of space (measured in points) between the edge of the view and any subviews. Auto layout uses your margins as a cue for placing content. For example, if you specify a set of horizontal constraints using the format string “`|-[subview]-|`”, the left and right edges of the subview are inset from the edge of the superview by the corresponding layout margins. When the edge of your view is close to the edge of the superview and the [`preservesSuperviewLayoutMargins`](uiview/preservessuperviewlayoutmargins.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), the actual layout margins may be increased to prevent content from overlapping the superview’s margins.

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](uiview/directionallayoutmargins.md)
  The default spacing to use when laying out content in a view, taking into account the current language direction.
- [var preservesSuperviewLayoutMargins: Bool](uiview/preservessuperviewlayoutmargins.md)
  A Boolean value indicating whether the current view also respects the margins of its superview.
- [func layoutMarginsDidChange()](uiview/layoutmarginsdidchange.md)
  Notifies the view that the layout margins changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layoutmargins)*