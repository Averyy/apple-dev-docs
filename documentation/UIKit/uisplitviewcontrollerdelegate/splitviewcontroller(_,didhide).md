# splitViewController(_:didHide:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system completed hiding the specified column.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional func splitViewController(_ svc: UISplitViewController, didHide column: UISplitViewController.Column)
```

```objc
- (void) splitViewController:(UISplitViewController *) svc didHideColumn:(UISplitViewControllerColumn) column;
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the system completes hiding one of its columns; for example, when a person rotates the device. The system doesn’t call this method when you hide a column programmatically with [`hide(_:)`](../uisplitviewcontroller/hide%28_%29.md). Use this method to perform any updates after hiding the column. You can use the split view controller’s [`transitionCoordinator`](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `svc`: The split view controller whose column the system completed hiding.
- `column`: The column the system completed hiding. See [`UISplitViewController.Column`](../uisplitviewcontroller/column.md) for possible values.

## See Also

### Collapsing the interface
- [func splitViewController(UISplitViewController, topColumnForCollapsingToProposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column](./splitviewcontroller%28_,topcolumnforcollapsingtoproposedtopcolumn%29.md)
  Asks the delegate to provide the column to display after the split view interface collapses.
- [func splitViewController(UISplitViewController, willHide: UISplitViewController.Column)](./splitviewcontroller%28_,willhide%29.md)
  Tells the delegate that the specified column is about to be hidden.
- [func splitViewControllerDidCollapse(UISplitViewController)](./splitviewcontrollerdidcollapse%28_%29.md)
  Tells the delegate that the split view controller interface has collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:didhide:))*