# splitViewController(_:willShow:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified column is about to be shown.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func splitViewController(_ svc: UISplitViewController, willShow column: UISplitViewController.Column)
```

```objc
- (void) splitViewController:(UISplitViewController *) svc willShowColumn:(UISplitViewControllerColumn) column;
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the system is preparing to show one of its columns; for example, when a person rotates the device. The system doesn’t call this method when you display the column programmatically with [`show(_:)`](../uisplitviewcontroller/show%28_%29.md). Use this method to perform any customization associated with showing the column. You can use the split view controller’s [`transitionCoordinator`](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `svc`: The split view controller whose column is being shown.
- `column`: The column to be shown. See [`UISplitViewController.Column`](../uisplitviewcontroller/column.md) for possible values.

## See Also

### Expanding the interface
- [func splitViewController(UISplitViewController, displayModeForExpandingToProposedDisplayMode: UISplitViewController.DisplayMode) -> UISplitViewController.DisplayMode](./splitviewcontroller%28_,displaymodeforexpandingtoproposeddisplaymode%29.md)
  Asks the delegate to provide the display mode to use after the split view interface expands.
- [func splitViewController(UISplitViewController, didShow: UISplitViewController.Column)](./splitviewcontroller%28_,didshow%29.md)
  Tells the delegate that the system completed showing the specified column.
- [func splitViewControllerDidExpand(UISplitViewController)](./splitviewcontrollerdidexpand%28_%29.md)
  Tells the delegate that the split view controller interface has expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:))*