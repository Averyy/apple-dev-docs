# tableView(_:performAction:forRowAt:withSender:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate to perform a copy or paste operation on the content of a given row.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAt indexPath: IndexPath, withSender sender: Any?)
```

#### Discussion

The table view invokes this method for a given `action` if the user taps Copy or Paste in the editing menu. The delegate can do whatever is appropriate for the action; for example, for a copy, it can extract the relevant cell content for the row at `indexPath` and write it to the general pasteboard or an application (private) pasteboard. See [`UIPasteboard`](uipasteboard.md) for further information.

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
- [func tableView(UITableView, canPerformAction: Selector, forRowAt: IndexPath, withSender: Any?) -> Bool](uitableviewdelegate/tableview(_:canperformaction:forrowat:withsender:).md)
  Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.
- [func tableView(UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]?](uitableviewdelegate/tableview(_:editactionsforrowat:).md)
  Asks the delegate for the actions to display in response to a swipe in the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:performaction:forrowat:withsender:))*