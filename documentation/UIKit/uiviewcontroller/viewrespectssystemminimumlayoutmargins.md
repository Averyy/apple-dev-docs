# viewRespectsSystemMinimumLayoutMargins

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view controller’s view uses the system-defined minimum layout margins.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var viewRespectsSystemMinimumLayoutMargins: Bool { get set }
```

```objc
@property (nonatomic) BOOL viewRespectsSystemMinimumLayoutMargins;
```

## Mentions

- [Positioning content within layout margins](../positioning-content-within-layout-margins.md)

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the root view’s layout margins are guaranteed to be no smaller than the values in the [`systemMinimumLayoutMargins`](./systemminimumlayoutmargins.md) property. The default value of this property is [`true`](../../Swift/true.md).

Changing this property to [`false`](../../Swift/false.md) causes the view to obtain its margins solely from its [`directionalLayoutMargins`](../uiview/directionallayoutmargins.md) property. Setting the margins in that property to `0` allows you to eliminate the view’s margins altogether.

## See Also

### Managing the view’s margins
- [Positioning content within layout margins](../positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](./systemminimumlayoutmargins.md)
  The minimum layout margins for the view controller’s root view.
- [func viewLayoutMarginsDidChange()](./viewlayoutmarginsdidchange%28%29.md)
  Called to notify the view controller that the layout margins of its root view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewrespectssystemminimumlayoutmargins)*