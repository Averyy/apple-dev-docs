# tableView(_:shouldShowMenuForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the editing menu should be shown for a certain row.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

## Declaration

```swift
optional func tableView(_ tableView: UITableView, shouldShowMenuForRowAt indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView shouldShowMenuForRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

[`true`](../../Swift/true.md) if the editing menu should be shown positioned near the row and pointing to it, otherwise [`false`](../../Swift/false.md). The default value is [`false`](../../Swift/false.md).

## Discussion

If the user tap-holds a certain row in the table view, this method (if implemented) is invoked first. Return [`false`](../../Swift/false.md) if the editing menu shouldn’t be shown—for example, the cell corresponding to the row contains content that shouldn’t be copied or pasted over.

## Parameters

- `tableView`: The table view that is making this request.
- `indexPath`: The index path of the row.

## See Also

### Deprecated
- [func tableView(UITableView, canPerformAction: Selector, forRowAt: IndexPath, withSender: Any?) -> Bool](./tableview%28_,canperformaction,forrowat,withsender%29.md)
  Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.
- [func tableView(UITableView, performAction: Selector, forRowAt: IndexPath, withSender: Any?)](./tableview%28_,performaction,forrowat,withsender%29.md)
  Tells the delegate to perform a copy or paste operation on the content of a given row.
- [func tableView(UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]?](./tableview%28_,editactionsforrowat%29.md)
  Asks the delegate for the actions to display in response to a swipe in the specified row.
- [- tableView:accessoryTypeForRowWithIndexPath:](./tableview_accessorytypeforrowwithindexpath_.md)
  Asks the delegate for the type of standard accessory view to use as a disclosure control for the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldshowmenuforrowat:))*