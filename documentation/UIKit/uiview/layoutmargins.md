# layoutMargins

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The default spacing to use when laying out content in the view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var layoutMargins: UIEdgeInsets { get set }
```

```objc
@property (nonatomic) UIEdgeInsets layoutMargins;
```

#### Discussion

In iOS 11 and later, use the [`directionalLayoutMargins`](./directionallayoutmargins.md) property to specify layout margins instead of this property. The leading and trailing edge insets in the [`directionalLayoutMargins`](./directionallayoutmargins.md) property are synchronized with the left and right insets in this property. For example, setting the [`leading`](../nsdirectionaledgeinsets/leading.md) directional edge inset to 20 points causes the [`left`](../uiedgeinsets/left.md) inset of this property to be set to 20 points on a system with a left-to-right language.

For the root view of a view controller, the default value of this property reflects the system minimum margins and safe area insets. For other subviews in your view hierarchy, the values may be greater if the view is not fully inside the safe area or if the [`preservesSuperviewLayoutMargins`](./preservessuperviewlayoutmargins.md) property is [`true`](../../Swift/true.md).

This property specifies the desired amount of space (measured in points) between the edge of the view and any subviews. Auto layout uses your margins as a cue for placing content. For example, if you specify a set of horizontal constraints using the format string “`|-[subview]-|`”, the left and right edges of the subview are inset from the edge of the superview by the corresponding layout margins. When the edge of your view is close to the edge of the superview and the [`preservesSuperviewLayoutMargins`](./preservessuperviewlayoutmargins.md) property is [`true`](../../Swift/true.md), the actual layout margins may be increased to prevent content from overlapping the superview’s margins.

## See Also

### Configuring content margins
- [Positioning content within layout margins](../positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](./directionallayoutmargins.md)
  The default spacing to use when laying out content in a view, taking into account the current language direction.
- [var preservesSuperviewLayoutMargins: Bool](./preservessuperviewlayoutmargins.md)
  A Boolean value indicating whether the current view also respects the margins of its superview.
- [func layoutMarginsDidChange()](./layoutmarginsdidchange%28%29.md)
  Notifies the view that the layout margins changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layoutmargins)*