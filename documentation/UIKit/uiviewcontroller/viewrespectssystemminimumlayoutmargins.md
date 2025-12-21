# viewRespectsSystemMinimumLayoutMargins

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the view controller’s view uses the system-defined minimum layout margins.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var viewRespectsSystemMinimumLayoutMargins: Bool { get set }
```

## Mentions

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the root view’s layout margins are guaranteed to be no smaller than the values in the [`systemMinimumLayoutMargins`](uiviewcontroller/systemminimumlayoutmargins.md) property. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

Changing this property to [`false`](https://developer.apple.com/documentation/Swift/false) causes the view to obtain its margins solely from its [`directionalLayoutMargins`](uiview/directionallayoutmargins.md) property. Setting the margins in that property to `0` allows you to eliminate the view’s margins altogether.

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](uiviewcontroller/systemminimumlayoutmargins.md)
  The minimum layout margins for the view controller’s root view.
- [func viewLayoutMarginsDidChange()](uiviewcontroller/viewlayoutmarginsdidchange.md)
  Called to notify the view controller that the layout margins of its root view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewrespectssystemminimumlayoutmargins)*