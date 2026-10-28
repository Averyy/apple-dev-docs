# tableView(_:performAction:forRowAt:withSender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to perform a copy or paste operation on the content of a given row.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

## Declaration

```swift
optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAt indexPath: IndexPath, withSender sender: Any?)
```

```objc
- (void) tableView:(UITableView *) tableView performAction:(SEL) action forRowAtIndexPath:(NSIndexPath *) indexPath withSender:(id) sender;
```

## Discussion

The table view invokes this method for a given `action` if the user taps Copy or Paste in the editing menu. The delegate can do whatever is appropriate for the action; for example, for a copy, it can extract the relevant cell content for the row at `indexPath` and write it to the general pasteboard or an application (private) pasteboard. See [`UIPasteboard`](../uipasteboard.md) for further information.

## Parameters

- `tableView`: The table view that is making this request.
- `action`: A selector type identifying the [`copy(_:)`](../uiresponderstandardeditactions/copy%28_%29.md) or [`paste(_:)`](../uiresponderstandardeditactions/paste%28_%29.md) method of the [`UIResponderStandardEditActions`](../uiresponderstandardeditactions.md) informal protocol.
- `indexPath`: The index path of the row.
- `sender`: The object that initially sent the `copy:` or `paste:` message.

## See Also

### Deprecated
- [func tableView(UITableView, shouldShowMenuForRowAt: IndexPath) -> Bool](./tableview%28_,shouldshowmenuforrowat%29.md)
  Asks the delegate if the editing menu should be shown for a certain row.
- [func tableView(UITableView, canPerformAction: Selector, forRowAt: IndexPath, withSender: Any?) -> Bool](./tableview%28_,canperformaction,forrowat,withsender%29.md)
  Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.
- [func tableView(UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]?](./tableview%28_,editactionsforrowat%29.md)
  Asks the delegate for the actions to display in response to a swipe in the specified row.
- [- tableView:accessoryTypeForRowWithIndexPath:](./tableview_accessorytypeforrowwithindexpath_.md)
  Asks the delegate for the type of standard accessory view to use as a disclosure control for the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:performaction:forrowat:withsender:))*