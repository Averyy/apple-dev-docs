# tableView(_:willBeginEditingRowAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the table view is about to go into editing mode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, willBeginEditingRowAt indexPath: IndexPath)
```

#### Discussion

This method is called when the user swipes horizontally across a row; as a consequence, the table view sets its [`isEditing`](uitableview/isediting.md) property to [`true`](https://developer.apple.com/documentation/swift/true) (thereby entering editing mode) and displays a Delete button in the row identified by `indexPath`. In this “swipe to delete” mode the table view does not display any insertion, deletion, and reordering controls. This method gives the delegate an opportunity to adjust the application’s user interface to editing mode. When the table exits editing mode (for example, the user taps the Delete button), the table view calls [`tableView(_:didEndEditingRowAt:)`](uitableviewdelegate/tableview(_:didendeditingrowat:).md).

> **Note**:  A swipe motion across a cell does not cause the display of a Delete button unless the table view’s data source implements the [`tableView(_:commit:forRowAt:)`](uitableviewdatasource/tableview(_:commit:forrowat:).md) method.

## Parameters

- `tableView`: The table view providing this information.
- `indexPath`: An index path locating the row in  .

## See Also

- [func tableView(UITableView, didEndEditingRowAt: IndexPath?)](uitableviewdelegate/tableview(_:didendeditingrowat:).md)
  Tells the delegate that the table view has left editing mode.
- [func tableView(UITableView, editingStyleForRowAt: IndexPath) -> UITableViewCell.EditingStyle](uitableviewdelegate/tableview(_:editingstyleforrowat:).md)
  Asks the delegate for the editing style of a row at a particular location in a table view.
- [func tableView(UITableView, titleForDeleteConfirmationButtonForRowAt: IndexPath) -> String?](uitableviewdelegate/tableview(_:titlefordeleteconfirmationbuttonforrowat:).md)
  Changes the default title of the delete-confirmation button.
- [func tableView(UITableView, shouldIndentWhileEditingRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldindentwhileeditingrowat:).md)
  Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willbegineditingrowat:))*