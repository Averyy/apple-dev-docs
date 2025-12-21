# systemMinimumLayoutMargins

**Framework**: UIKit  
**Kind**: property

The minimum layout margins for the view controller’s root view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var systemMinimumLayoutMargins: NSDirectionalEdgeInsets { get }
```

## Mentions

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)

#### Discussion

This property contains the minimum layout margins expected by the system for the view controller’s root view. Do not override this property. To stop considering the system’s minimum layout margins for the root view, set the [`viewRespectsSystemMinimumLayoutMargins`](uiviewcontroller/viewrespectssystemminimumlayoutmargins.md) property to [`false`](https://developer.apple.com/documentation/Swift/false). This property does not affect the margins associated with subviews of the root view.

If you assign a custom value to the [`directionalLayoutMargins`](uiview/directionallayoutmargins.md) property of the view controller’s root view, the root view’s actual margins are set to either your custom values or the minimum values defined by this property, whichever values are greater. For example, if the value for one system minimum margin is `20` points and you specify a value of `10` for the same margin on the view, the view uses the value `20` for the margin.

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var viewRespectsSystemMinimumLayoutMargins: Bool](uiviewcontroller/viewrespectssystemminimumlayoutmargins.md)
  A Boolean value indicating whether the view controller’s view uses the system-defined minimum layout margins.
- [func viewLayoutMarginsDidChange()](uiviewcontroller/viewlayoutmarginsdidchange.md)
  Called to notify the view controller that the layout margins of its root view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/systemminimumlayoutmargins)*