# tableView(_:editingStyleForRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the editing style of a row at a particular location in a table view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, editingStyleForRowAt indexPath: IndexPath) -> UITableViewCell.EditingStyle
```

#### Return Value

The editing style of the cell for the row identified by `indexPath`.

#### Discussion

This method allows the delegate to customize the editing style of the cell located at`indexPath`. If the delegate does not implement this method and the `UITableViewCell` object is editable (that is, it has its [`isEditing`](uitableviewcell/isediting.md) property set to [`true`](https://developer.apple.com/documentation/Swift/true)), the cell has the [`UITableViewCell.EditingStyle.delete`](uitableviewcell/editingstyle-swift.enum/delete.md) style set for it.

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path locating a row in  .

## See Also

- [func tableView(UITableView, willBeginEditingRowAt: IndexPath)](uitableviewdelegate/tableview(_:willbegineditingrowat:).md)
  Tells the delegate that the table view is about to go into editing mode.
- [func tableView(UITableView, didEndEditingRowAt: IndexPath?)](uitableviewdelegate/tableview(_:didendeditingrowat:).md)
  Tells the delegate that the table view has left editing mode.
- [func tableView(UITableView, titleForDeleteConfirmationButtonForRowAt: IndexPath) -> String?](uitableviewdelegate/tableview(_:titlefordeleteconfirmationbuttonforrowat:).md)
  Changes the default title of the delete-confirmation button.
- [func tableView(UITableView, shouldIndentWhileEditingRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldindentwhileeditingrowat:).md)
  Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:editingstyleforrowat:))*