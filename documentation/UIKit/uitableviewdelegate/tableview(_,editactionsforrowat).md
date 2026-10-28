# tableView(_:editActionsForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the actions to display in response to a swipe in the specified row.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
optional func tableView(_ tableView: UITableView, editActionsForRowAt indexPath: IndexPath) -> [UITableViewRowAction]?
```

```objc
- (NSArray<UITableViewRowAction *> *) tableView:(UITableView *) tableView editActionsForRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

An array of [`UITableViewRowAction`](../uitableviewrowaction.md) objects representing the actions for the row. Each action you provide is used to create a button that the user can tap.

## Discussion

Use this method when you want to provide custom actions for one of your table rows. When the user swipes horizontally in a row, the table view moves the row content aside to reveal your actions. Tapping one of the action buttons executes the handler block stored with the action object.

If you do not implement this method, the table view displays the standard accessory buttons when the user swipes the row.

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: The index path of the row.

## See Also

### Deprecated
- [func tableView(UITableView, shouldShowMenuForRowAt: IndexPath) -> Bool](./tableview%28_,shouldshowmenuforrowat%29.md)
  Asks the delegate if the editing menu should be shown for a certain row.
- [func tableView(UITableView, canPerformAction: Selector, forRowAt: IndexPath, withSender: Any?) -> Bool](./tableview%28_,canperformaction,forrowat,withsender%29.md)
  Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.
- [func tableView(UITableView, performAction: Selector, forRowAt: IndexPath, withSender: Any?)](./tableview%28_,performaction,forrowat,withsender%29.md)
  Tells the delegate to perform a copy or paste operation on the content of a given row.
- [- tableView:accessoryTypeForRowWithIndexPath:](./tableview_accessorytypeforrowwithindexpath_.md)
  Asks the delegate for the type of standard accessory view to use as a disclosure control for the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:editactionsforrowat:))*