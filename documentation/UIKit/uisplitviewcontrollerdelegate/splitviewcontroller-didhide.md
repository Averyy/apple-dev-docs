# splitViewController(_:didHide:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the system completed hiding the specified column.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, didHide column: UISplitViewController.Column)
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

The split view controller calls this method when the system completes hiding one of its columns; for example, when a person rotates the device. The system doesn’t call this method when you hide a column programmatically with [`hide(_:)`](uisplitviewcontroller/hide(_:).md). Use this method to perform any updates after hiding the column. You can use the split view controller’s [`transitionCoordinator`](uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `svc`: The split view controller whose column the system completed hiding.
- `column`: The column the system completed hiding. See   for possible values.

## See Also

- [func splitViewController(UISplitViewController, topColumnForCollapsingToProposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column](uisplitviewcontrollerdelegate/splitviewcontroller(_:topcolumnforcollapsingtoproposedtopcolumn:).md)
  Asks the delegate to provide the column to display after the split view interface collapses.
- [func splitViewController(UISplitViewController, willHide: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:).md)
  Tells the delegate that the specified column is about to be hidden.
- [func splitViewControllerDidCollapse(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(_:).md)
  Tells the delegate that the split view controller interface has collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:didhide:))*