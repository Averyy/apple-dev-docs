# tableView(_:commit:forRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the data source to commit the insertion or deletion of a specified row.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath)
```

#### Discussion

When users tap the insertion (green plus) control or Delete button associated with a [`UITableViewCell`](uitableviewcell.md) object in the table view, the table view sends this message to the data source, asking it to commit the change. (If the user taps the deletion (red minus) control, the table view then displays the Delete button to get confirmation.) The data source commits the insertion or deletion by invoking the `UITableView` methods [`insertRows(at:with:)`](uitableview/insertrows(at:with:).md) or [`deleteRows(at:with:)`](uitableview/deleterows(at:with:).md), as appropriate.

To enable the swipe-to-delete feature of table views (wherein a user swipes horizontally across a row to display a Delete button), you must implement this method.

You shouldn’t call [`setEditing(_:animated:)`](uitableview/setediting(_:animated:).md) within an implementation of this method. If for some reason you must, invoke it after a delay by using the [`perform(_:with:afterDelay:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/perform(_:with:afterDelay:)) method.

## Parameters

- `tableView`: The table-view object requesting the insertion or deletion.
- `editingStyle`: The cell editing style corresponding to a insertion or deletion requested for the row specified by  . Possible editing styles are   or  .
- `indexPath`: An index path locating the row in  .

## See Also

- [func tableView(UITableView, canEditRowAt: IndexPath) -> Bool](uitableviewdatasource/tableview(_:caneditrowat:).md)
  Asks the data source to verify that the given row is editable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:commit:forrowat:))*