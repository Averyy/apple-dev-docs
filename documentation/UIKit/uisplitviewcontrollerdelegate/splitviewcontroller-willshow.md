# splitViewController(_:willShow:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified column is about to be shown.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, willShow column: UISplitViewController.Column)
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

The split view controller calls this method when one of its columns is about to be shown, for example with [`show(_:)`](uisplitviewcontroller/show(_:).md). Use this method to perform any customization associated with showing the column. You can use the split view controller’s [`transitionCoordinator`](uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `svc`: The split view controller whose column is being shown.
- `column`: The column to be shown. See   for possible values.

## See Also

- [func splitViewController(UISplitViewController, displayModeForExpandingToProposedDisplayMode: UISplitViewController.DisplayMode) -> UISplitViewController.DisplayMode](uisplitviewcontrollerdelegate/splitviewcontroller(_:displaymodeforexpandingtoproposeddisplaymode:).md)
  Asks the delegate to provide the display mode to use after the split view interface expands.
- [func splitViewControllerDidExpand(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(_:).md)
  Tells the delegate that the split view controller interface has expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:))*