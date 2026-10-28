# tableView(_:moveRowAt:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the data source to move a row at a specific location in the table view to another location.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, moveRowAt sourceIndexPath: IndexPath, to destinationIndexPath: IndexPath)
```

```objc
- (void) tableView:(UITableView *) tableView moveRowAtIndexPath:(NSIndexPath *) sourceIndexPath toIndexPath:(NSIndexPath *) destinationIndexPath;
```

## Discussion

The [`UITableView`](../uitableview.md) object sends this message to the data source when the user presses the reorder control in the row at `sourceIndexPath`.

## Parameters

- `tableView`: The table-view object requesting this action.
- `sourceIndexPath`: An index path locating the row to be moved in `tableView`.
- `destinationIndexPath`: An index path locating the row in `tableView` that’s the destination of the move.

## See Also

### Related Documentation
- [func tableView(UITableView, commit: UITableViewCell.EditingStyle, forRowAt: IndexPath)](./tableview%28_,commit,forrowat%29.md)
  Asks the data source to commit the insertion or deletion of a specified row.
### Reordering table rows
- [func tableView(UITableView, canMoveRowAt: IndexPath) -> Bool](./tableview%28_,canmoverowat%29.md)
  Asks the data source whether a given row can move to another location in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:moverowat:to:))*