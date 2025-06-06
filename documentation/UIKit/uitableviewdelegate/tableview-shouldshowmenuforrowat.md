# tableView(_:shouldShowMenuForRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the editing menu should be shown for a certain row.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, shouldShowMenuForRowAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the editing menu should be shown positioned near the row and pointing to it, otherwise [`false`](https://developer.apple.com/documentation/swift/false). The default value is [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the user tap-holds a certain row in the table view, this method (if implemented) is invoked first. Return [`false`](https://developer.apple.com/documentation/swift/false) if the editing menu shouldn’t be shown—for example, the cell corresponding to the row contains content that shouldn’t be copied or pasted over.

## Parameters

- `tableView`: The table view that is making this request.
- `indexPath`: The index path of the row.

## See Also

- [func tableView(UITableView, leadingSwipeActionsConfigurationForRowAt: IndexPath) -> UISwipeActionsConfiguration?](uitableviewdelegate/tableview(_:leadingswipeactionsconfigurationforrowat:).md)
  Returns the swipe actions to display on the leading edge of the row.
- [func tableView(UITableView, trailingSwipeActionsConfigurationForRowAt: IndexPath) -> UISwipeActionsConfiguration?](uitableviewdelegate/tableview(_:trailingswipeactionsconfigurationforrowat:).md)
  Returns the swipe actions to display on the trailing edge of the row.
- [func tableView(UITableView, canPerformAction: Selector, forRowAt: IndexPath, withSender: Any?) -> Bool](uitableviewdelegate/tableview(_:canperformaction:forrowat:withsender:).md)
  Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.
- [func tableView(UITableView, performAction: Selector, forRowAt: IndexPath, withSender: Any?)](uitableviewdelegate/tableview(_:performaction:forrowat:withsender:).md)
  Tells the delegate to perform a copy or paste operation on the content of a given row.
- [func tableView(UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]?](uitableviewdelegate/tableview(_:editactionsforrowat:).md)
  Asks the delegate for the actions to display in response to a swipe in the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldshowmenuforrowat:))*