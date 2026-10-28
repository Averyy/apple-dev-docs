# tableView(_:canPerformAction:forRowAt:withSender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

## Declaration

```swift
optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAt indexPath: IndexPath, withSender sender: Any?) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView canPerformAction:(SEL) action forRowAtIndexPath:(NSIndexPath *) indexPath withSender:(id) sender;
```

## Return Value

[`true`](../../Swift/true.md) if the command corresponding to `action` should appear in the editing menu, otherwise [`false`](../../Swift/false.md). The default value is [`false`](../../Swift/false.md).

## Discussion

This method is invoked after [`tableView(_:shouldShowMenuForRowAt:)`](./tableview%28_,shouldshowmenuforrowat%29.md). It gives the developer the opportunity to exclude one of the commands—Copy or Paste—from the editing menu. For example, the user might have copied some cell content from one row but wants to paste into another row that doesn’t take the copied content. In a case like this, return [`false`](../../Swift/false.md) from this method.

## Parameters

- `tableView`: The table view that is making this request.
- `action`: A selector type identifying the [`copy(_:)`](../uiresponderstandardeditactions/copy%28_%29.md) or [`paste(_:)`](../uiresponderstandardeditactions/paste%28_%29.md) method of the [`UIResponderStandardEditActions`](../uiresponderstandardeditactions.md) informal protocol.
- `indexPath`: The index path of the row.
- `sender`: The object that initially sent the `copy:` or `paste:` message.

## See Also

### Deprecated
- [func tableView(UITableView, shouldShowMenuForRowAt: IndexPath) -> Bool](./tableview%28_,shouldshowmenuforrowat%29.md)
  Asks the delegate if the editing menu should be shown for a certain row.
- [func tableView(UITableView, performAction: Selector, forRowAt: IndexPath, withSender: Any?)](./tableview%28_,performaction,forrowat,withsender%29.md)
  Tells the delegate to perform a copy or paste operation on the content of a given row.
- [func tableView(UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]?](./tableview%28_,editactionsforrowat%29.md)
  Asks the delegate for the actions to display in response to a swipe in the specified row.
- [- tableView:accessoryTypeForRowWithIndexPath:](./tableview_accessorytypeforrowwithindexpath_.md)
  Asks the delegate for the type of standard accessory view to use as a disclosure control for the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:canperformaction:forrowat:withsender:))*