# splitViewController(_:displayModeForExpandingToProposedDisplayMode:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to provide the display mode to use after the split view interface expands.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, displayModeForExpandingToProposedDisplayMode proposedDisplayMode: UISplitViewController.DisplayMode) -> UISplitViewController.DisplayMode
```

#### Return Value

The display mode to expand the interface to. This value may be the same as `proposedDisplayMode`, or you may return a different value.

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

When the split view controller transitions from a horizontally compact to a horizontally regular size class, it calls this method and asks you for the display mode to use when that transition is complete. Use this method to customize the display mode you’re expanding to. For example, you might use this opportunity to adjust column widths before returning the display mode to use.

## Parameters

- `svc`: The split view controller whose interface is expanding.
- `proposedDisplayMode`: The proposed display mode to expand the interface to.

## See Also

- [func splitViewController(UISplitViewController, willShow: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:).md)
  Tells the delegate that the specified column is about to be shown.
- [func splitViewControllerDidExpand(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(_:).md)
  Tells the delegate that the split view controller interface has expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:displaymodeforexpandingtoproposeddisplaymode:))*