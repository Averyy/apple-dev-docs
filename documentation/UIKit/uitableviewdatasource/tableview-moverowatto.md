# tableView(_:moveRowAt:to:)

**Framework**: UIKit  
**Kind**: method

Tells the data source to move a row at a specific location in the table view to another location.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, moveRowAt sourceIndexPath: IndexPath, to destinationIndexPath: IndexPath)
```

#### Discussion

The [`UITableView`](uitableview.md) object sends this message to the data source when the user presses the reorder control in the row at `sourceIndexPath`.

## Parameters

- `tableView`: The table-view object requesting this action.
- `sourceIndexPath`: An index path locating the row to be moved in  .
- `destinationIndexPath`: An index path locating the row in   that’s the destination of the move.

## See Also

- [func tableView(UITableView, commit: UITableViewCell.EditingStyle, forRowAt: IndexPath)](uitableviewdatasource/tableview(_:commit:forrowat:).md)
  Asks the data source to commit the insertion or deletion of a specified row.
- [func tableView(UITableView, canMoveRowAt: IndexPath) -> Bool](uitableviewdatasource/tableview(_:canmoverowat:).md)
  Asks the data source whether a given row can move to another location in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:moverowat:to:))*