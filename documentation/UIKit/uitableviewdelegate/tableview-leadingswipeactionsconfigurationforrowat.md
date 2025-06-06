# tableView(_:leadingSwipeActionsConfigurationForRowAt:)

**Framework**: UIKit  
**Kind**: method

Returns the swipe actions to display on the leading edge of the row.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, leadingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration?
```

#### Return Value

The swipe actions to display next to the leading edge of the row. Return `nil` if you want the table to display the default set of actions.

#### Discussion

Use this method to return a set of actions to display when the user swipes the row. The actions you return are displayed on the leading edge of the row. For example, in a left-to-right language environment, they are displayed on the left side of the row when the user swipes from left to right.

## Parameters

- `tableView`: The table view containing the row.
- `indexPath`: The index path of the row.

## See Also

- [func tableView(UITableView, trailingSwipeActionsConfigurationForRowAt: IndexPath) -> UISwipeActionsConfiguration?](uitableviewdelegate/tableview(_:trailingswipeactionsconfigurationforrowat:).md)
  Returns the swipe actions to display on the trailing edge of the row.
- [func tableView(UITableView, shouldShowMenuForRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldshowmenuforrowat:).md)
  Asks the delegate if the editing menu should be shown for a certain row.
- [func tableView(UITableView, canPerformAction: Selector, forRowAt: IndexPath, withSender: Any?) -> Bool](uitableviewdelegate/tableview(_:canperformaction:forrowat:withsender:).md)
  Asks the delegate if the editing menu should omit the Copy or Paste command for a given row.
- [func tableView(UITableView, performAction: Selector, forRowAt: IndexPath, withSender: Any?)](uitableviewdelegate/tableview(_:performaction:forrowat:withsender:).md)
  Tells the delegate to perform a copy or paste operation on the content of a given row.
- [func tableView(UITableView, editActionsForRowAt: IndexPath) -> [UITableViewRowAction]?](uitableviewdelegate/tableview(_:editactionsforrowat:).md)
  Asks the delegate for the actions to display in response to a swipe in the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:leadingswipeactionsconfigurationforrowat:))*