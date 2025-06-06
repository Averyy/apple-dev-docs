# preservesSuperviewLayoutMargins

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the current view also respects the margins of its superview.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preservesSuperviewLayoutMargins: Bool { get set }
```

## Mentions

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the superview’s margins are also considered when laying out content. This margin affects layouts where the distance between the edge of a view and its superview is smaller than the corresponding margin. For example, you might have a content view whose frame precisely matches the bounds of its superview. When any of the superview’s margins is inside the area represented by the content view and its own margins, UIKit adjusts the content view’s layout to respect the superview’s margins. The amount of the adjustment is the smallest amount needed to ensure that content is also inside the superview’s margins.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](uiview/directionallayoutmargins.md)
  The default spacing to use when laying out content in a view, taking into account the current language direction.
- [var layoutMargins: UIEdgeInsets](uiview/layoutmargins.md)
  The default spacing to use when laying out content in the view.
- [func layoutMarginsDidChange()](uiview/layoutmarginsdidchange.md)
  Notifies the view that the layout margins changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/preservessuperviewlayoutmargins)*