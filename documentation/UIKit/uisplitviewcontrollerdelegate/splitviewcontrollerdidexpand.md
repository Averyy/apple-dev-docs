# splitViewControllerDidExpand(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the split view controller interface has expanded.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewControllerDidExpand(_ svc: UISplitViewController)
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

The split view controller calls this method after its interface has expanded, meaning that [`isCollapsed`](uisplitviewcontroller/iscollapsed.md) is [`false`](https://developer.apple.com/documentation/Swift/false). Use this method to perform any customization associated with the expanded interface.

## Parameters

- `svc`: The split view controller whose interface has expanded.

## See Also

- [func splitViewController(UISplitViewController, displayModeForExpandingToProposedDisplayMode: UISplitViewController.DisplayMode) -> UISplitViewController.DisplayMode](uisplitviewcontrollerdelegate/splitviewcontroller(_:displaymodeforexpandingtoproposeddisplaymode:).md)
  Asks the delegate to provide the display mode to use after the split view interface expands.
- [func splitViewController(UISplitViewController, willShow: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:).md)
  Tells the delegate that the specified column is about to be shown.
- [func splitViewController(UISplitViewController, didShow: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:didshow:).md)
  Tells the delegate that the system completed showing the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(_:))*