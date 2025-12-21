# splitViewController(_:topColumnForCollapsingToProposedTopColumn:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to provide the column to display after the split view interface collapses.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, topColumnForCollapsingToProposedTopColumn proposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column
```

#### Return Value

The column corresponding to the view controller to display in the collapsed interface. This value may be the same as `proposedTopColumn`, or you may return a different value.

#### Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

When the split view controller transitions from a horizontally regular to a horizontally compact size class, it calls this method and asks you for the column to display when that transition is complete. Use this method to customize the view controller you’re collapsing to. For example, you might use this opportunity to configure the interface in the view controller associated with the [`UISplitViewController.Column.compact`](uisplitviewcontroller/column/compact.md) column before returning that column.

## Parameters

- `svc`: The split view controller whose interface is collapsing.
- `proposedTopColumn`: The proposed column to display in the collapsed interface.

## See Also

- [func splitViewController(UISplitViewController, willHide: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:).md)
  Tells the delegate that the specified column is about to be hidden.
- [func splitViewController(UISplitViewController, didHide: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:didhide:).md)
  Tells the delegate that the system completed hiding the specified column.
- [func splitViewControllerDidCollapse(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(_:).md)
  Tells the delegate that the split view controller interface has collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:topcolumnforcollapsingtoproposedtopcolumn:))*