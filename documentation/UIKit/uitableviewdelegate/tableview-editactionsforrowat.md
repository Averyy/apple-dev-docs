# tableView(_:editActionsForRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the actions to display in response to a swipe in the specified row.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, editActionsForRowAt indexPath: IndexPath) -> [UITableViewRowAction]?
```

#### Return Value

An array of [`UITableViewRowAction`](uitableviewrowaction.md) objects representing the actions for the row. Each action you provide is used to create a button that the user can tap.

#### Discussion

Use this method when you want to provide custom actions for one of your table rows. When the user swipes horizontally in a row, the table view moves the row content aside to reveal your actions. Tapping one of the action buttons executes the handler block stored with the action object.

If you do not implement this method, the table view displays the standard accessory buttons when the user swipes the row.

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: The index path of the row.

## See Also

- [func tableView(UITableView, leadingSwipeActionsConfigurationForRowAt: IndexPath) -> UISwipeActionsConfiguration?](uitableviewdelegate/tableview(_:leadingswipeactionsconfigurationforrowat:).md)
  Returns the swipe actions to display on the leading edge of the row.
- [func tableView(UITableView, trailingSwipeActionsConfigurationForRowAt: IndexPath) -> UISwipeActionsConfiguration?](uitableviewdelegate/tableview(_:trailingswipeactionsconfigurationforrowat:).md)
  Returns the swipe actions to display on the trailing edge of the row.
- [func tableView(UITableView, shouldShowMenuForRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldshowmenuforrowat:).md)
  Asks the delegate if the editing menu should be shown for a certain row.
- [func tableView(UITableView, canPerformAction: Selector, forRowAt: IndexPath, withSender: Any?) -> Bool](uitableviewdelegate/tableview(_:canperformaction:forrowat:withsender:).md)
  Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.
- [func tableView(UITableView, performAction: Selector, forRowAt: IndexPath, withSender: Any?)](uitableviewdelegate/tableview(_:performaction:forrowat:withsender:).md)
  Tells the delegate to perform a copy or paste operation on the content of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:editactionsforrowat:))*