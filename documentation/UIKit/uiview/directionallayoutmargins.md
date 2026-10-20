# directionalLayoutMargins

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The default spacing to use when laying out content in a view, taking into account the current language direction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var directionalLayoutMargins: NSDirectionalEdgeInsets { get set }
```

```objc
@property (nonatomic) NSDirectionalEdgeInsets directionalLayoutMargins;
```

## Mentions

- [Positioning content within layout margins](../positioning-content-within-layout-margins.md)

#### Discussion

Use this property to specify the desired amount of space (measured in points) between the edges of this view and its subviews. The system applies leading and trailing margins appropriately to the left or right margins based on the current layout direction. For example, the system applies the leading margin to the right edge of the view in right-to-left layouts. Set the margin values as needed for your interface.

For the root view of a view controller, the default value of this property reflects the system minimum margins and safe area insets. For other subviews in your view hierarchy, the values may be greater if the view is not fully inside the safe area or if the [`preservesSuperviewLayoutMargins`](./preservessuperviewlayoutmargins.md) property is [`true`](../../Swift/true.md).

Auto layout uses your margins as a cue for placing content. For example, if you specify a set of horizontal constraints using the format string “`|-[subview]-|`”, the leading and trailing edges of the subview are inset from the edge of the superview by the corresponding layout margins. When the edge of your view is close to the edge of the superview and the [`preservesSuperviewLayoutMargins`](./preservessuperviewlayoutmargins.md) property is true, the actual layout margins may be increased to prevent content from overlapping the superview’s margins.

## See Also

### Configuring content margins
- [Positioning content within layout margins](../positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var layoutMargins: UIEdgeInsets](./layoutmargins.md)
  The default spacing to use when laying out content in the view.
- [var preservesSuperviewLayoutMargins: Bool](./preservessuperviewlayoutmargins.md)
  A Boolean value indicating whether the current view also respects the margins of its superview.
- [func layoutMarginsDidChange()](./layoutmarginsdidchange%28%29.md)
  Notifies the view that the layout margins changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/directionallayoutmargins)*