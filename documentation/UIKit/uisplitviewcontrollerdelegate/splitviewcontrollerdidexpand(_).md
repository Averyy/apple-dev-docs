# splitViewControllerDidExpand(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the split view controller interface has expanded.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func splitViewControllerDidExpand(_ svc: UISplitViewController)
```

```objc
- (void) splitViewControllerDidExpand:(UISplitViewController *) svc;
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method after its interface has expanded, meaning that [`isCollapsed`](../uisplitviewcontroller/iscollapsed.md) is [`false`](../../Swift/false.md). Use this method to perform any customization associated with the expanded interface.

## Parameters

- `svc`: The split view controller whose interface has expanded.

## See Also

### Expanding the interface
- [func splitViewController(UISplitViewController, displayModeForExpandingToProposedDisplayMode: UISplitViewController.DisplayMode) -> UISplitViewController.DisplayMode](./splitviewcontroller%28_,displaymodeforexpandingtoproposeddisplaymode%29.md)
  Asks the delegate to provide the display mode to use after the split view interface expands.
- [func splitViewController(UISplitViewController, willShow: UISplitViewController.Column)](./splitviewcontroller%28_,willshow%29.md)
  Tells the delegate that the specified column is about to be shown.
- [func splitViewController(UISplitViewController, didShow: UISplitViewController.Column)](./splitviewcontroller%28_,didshow%29.md)
  Tells the delegate that the system completed showing the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(_:))*