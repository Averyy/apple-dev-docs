# tableView(_:canPerformAction:forRowAt:withSender:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAt indexPath: IndexPath, withSender sender: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the command corresponding to `action` should appear in the editing menu, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method is invoked after [`tableView(_:shouldShowMenuForRowAt:)`](uitableviewdelegate/tableview(_:shouldshowmenuforrowat:).md). It gives the developer the opportunity to exclude one of the commands—Copy or Paste—from the editing menu. For example, the user might have copied some cell content from one row but wants to paste into another row that doesn’t take the copied content. In a case like this, return [`false`](https://developer.apple.com/documentation/Swift/false) from this method.

## Parameters

- `tableView`: The table view that is making this request.
- `action`: A selector type identifying the   or   method of the   informal protocol.
- `indexPath`: The index path of the row.
- `sender`: The object that initially sent the   or   message.

## See Also

- [func tableView(UITableView, leadingSwipeActionsConfigurationForRowAt: IndexPath) -> UISwipeActionsConfiguration?](uitableviewdelegate/tableview(_:leadingswipeactionsconfigurationforrowat:).md)
  Returns the swipe actions to display on the leading edge of the row.
- [func tableView(UITableView, trailingSwipeActionsConfigurationForRowAt: IndexPath) -> UISwipeActionsConfiguration?](uitableviewdelegate/tableview(_:trailingswipeactionsconfigurationforrowat:).md)
  Returns the swipe actions to display on the trailing edge of the row.
- [func tableView(UITableView, shouldShowMenuForRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldshowmenuforrowat:).md)
  Asks the delegate if the editing menu should be shown for a certain row.
- [func tableView(UITableView, performAction: Selector, forRowAt: IndexPath, withSender: Any?)](uitableviewdelegate/tableview(_:performaction:forrowat:withsender:).md)
  Tells the delegate to perform a copy or paste operation on the content of a given row.
- [func tableView(UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]?](uitableviewdelegate/tableview(_:editactionsforrowat:).md)
  Asks the delegate for the actions to display in response to a swipe in the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:canperformaction:forrowat:withsender:))*