# splitViewController(_:willHide:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified column is about to be hidden.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, willHide column: UISplitViewController.Column)
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

The split view controller calls this method when the system is preparing to hide one of its columns; for example, when a person rotates the device. The system doesn’t call this method when you hide a column programmatically with [`hide(_:)`](uisplitviewcontroller/hide(_:).md). Use this method to perform any customization associated with hiding the column. You can use the split view controller’s [`transitionCoordinator`](uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `svc`: The split view controller whose column is being hidden.
- `column`: The column to be hidden. See   for possible values.

## See Also

- [func splitViewController(UISplitViewController, topColumnForCollapsingToProposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column](uisplitviewcontrollerdelegate/splitviewcontroller(_:topcolumnforcollapsingtoproposedtopcolumn:).md)
  Asks the delegate to provide the column to display after the split view interface collapses.
- [func splitViewController(UISplitViewController, didHide: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:didhide:).md)
  Tells the delegate that the system completed hiding the specified column.
- [func splitViewControllerDidCollapse(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(_:).md)
  Tells the delegate that the split view controller interface has collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:))*