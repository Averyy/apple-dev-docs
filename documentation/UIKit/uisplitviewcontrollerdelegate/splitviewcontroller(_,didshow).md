# splitViewController(_:didShow:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system completed showing the specified column.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional func splitViewController(_ svc: UISplitViewController, didShow column: UISplitViewController.Column)
```

```objc
- (void) splitViewController:(UISplitViewController *) svc didShowColumn:(UISplitViewControllerColumn) column;
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the system completes showing one of its columns; for example, when a person rotates the device. The system doesn’t call this method when you display the column programmatically with [`show(_:)`](../uisplitviewcontroller/show%28_%29.md). Use this method to perform any updates after  showing the column. You can use the split view controller’s [`transitionCoordinator`](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `svc`: The split view controller whose column the system completed showing.
- `column`: The column the system completed showing. See [`UISplitViewController.Column`](../uisplitviewcontroller/column.md) for possible values.

## See Also

### Expanding the interface
- [func splitViewController(UISplitViewController, displayModeForExpandingToProposedDisplayMode: UISplitViewController.DisplayMode) -> UISplitViewController.DisplayMode](./splitviewcontroller%28_,displaymodeforexpandingtoproposeddisplaymode%29.md)
  Asks the delegate to provide the display mode to use after the split view interface expands.
- [func splitViewController(UISplitViewController, willShow: UISplitViewController.Column)](./splitviewcontroller%28_,willshow%29.md)
  Tells the delegate that the specified column is about to be shown.
- [func splitViewControllerDidExpand(UISplitViewController)](./splitviewcontrollerdidexpand%28_%29.md)
  Tells the delegate that the split view controller interface has expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:didshow:))*