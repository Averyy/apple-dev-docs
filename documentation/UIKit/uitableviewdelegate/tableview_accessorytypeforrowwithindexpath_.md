# tableView:accessoryTypeForRowWithIndexPath:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the type of standard accessory view to use as a disclosure control for the specified row.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the accessory-view and accessory-type properties (for both normal and editing modes) of the [`UITableViewCell`](../uitableviewcell.md) class when configuring table-view cells.

## Declaration

```objc
- (UITableViewCellAccessoryType) tableView:(UITableView *) tableView accessoryTypeForRowWithIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

A constant identifying a type of standard accessory view. For details, see the “Constants” section in [`UITableViewCell`](../uitableviewcell.md).

## Parameters

- `tableView`: The table view requesting the accessory-view type.
- `indexPath`: An index path locating the row in `tableView`.

## See Also

### Deprecated
- [func tableView(UITableView, shouldShowMenuForRowAt: IndexPath) -> Bool](./tableview%28_,shouldshowmenuforrowat%29.md)
  Asks the delegate if the editing menu should be shown for a certain row.
- [func tableView(UITableView, canPerformAction: Selector, forRowAt: IndexPath, withSender: Any?) -> Bool](./tableview%28_,canperformaction,forrowat,withsender%29.md)
  Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.
- [func tableView(UITableView, performAction: Selector, forRowAt: IndexPath, withSender: Any?)](./tableview%28_,performaction,forrowat,withsender%29.md)
  Tells the delegate to perform a copy or paste operation on the content of a given row.
- [func tableView(UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]?](./tableview%28_,editactionsforrowat%29.md)
  Asks the delegate for the actions to display in response to a swipe in the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview:accessorytypeforrowwithindexpath:)*