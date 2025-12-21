# splitViewControllerDidCollapse(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the split view controller interface has collapsed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewControllerDidCollapse(_ svc: UISplitViewController)
```

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

The split view controller calls this method after its interface has collapsed, meaning that [`isCollapsed`](uisplitviewcontroller/iscollapsed.md) is [`true`](https://developer.apple.com/documentation/Swift/true). Use this method to perform any customization associated with the collapsed interface.

## Parameters

- `svc`: The split view controller whose interface has collapsed.

## See Also

- [func splitViewController(UISplitViewController, topColumnForCollapsingToProposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column](uisplitviewcontrollerdelegate/splitviewcontroller(_:topcolumnforcollapsingtoproposedtopcolumn:).md)
  Asks the delegate to provide the column to display after the split view interface collapses.
- [func splitViewController(UISplitViewController, willHide: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:).md)
  Tells the delegate that the specified column is about to be hidden.
- [func splitViewController(UISplitViewController, didHide: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:didhide:).md)
  Tells the delegate that the system completed hiding the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(_:))*