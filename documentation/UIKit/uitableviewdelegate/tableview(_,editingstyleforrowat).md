# tableView(_:editingStyleForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the editing style of a row at a particular location in a table view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, editingStyleForRowAt indexPath: IndexPath) -> UITableViewCell.EditingStyle
```

```objc
- (UITableViewCellEditingStyle) tableView:(UITableView *) tableView editingStyleForRowAtIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

The editing style of the cell for the row identified by `indexPath`.

#### Discussion

This method allows the delegate to customize the editing style of the cell located at`indexPath`. If the delegate does not implement this method and the `UITableViewCell` object is editable (that is, it has its [`isEditing`](../uitableviewcell/isediting.md) property set to [`true`](../../Swift/true.md)), the cell has the [`UITableViewCell.EditingStyle.delete`](../uitableviewcell/editingstyle-swift.enum/delete.md) style set for it.

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path locating a row in `tableView`.

## See Also

### Editing table rows
- [func tableView(UITableView, willBeginEditingRowAt: IndexPath)](./tableview%28_,willbegineditingrowat%29.md)
  Tells the delegate that the table view is about to go into editing mode.
- [func tableView(UITableView, didEndEditingRowAt: IndexPath?)](./tableview%28_,didendeditingrowat%29.md)
  Tells the delegate that the table view has left editing mode.
- [func tableView(UITableView, titleForDeleteConfirmationButtonForRowAt: IndexPath) -> String?](./tableview%28_,titlefordeleteconfirmationbuttonforrowat%29.md)
  Changes the default title of the delete-confirmation button.
- [func tableView(UITableView, shouldIndentWhileEditingRowAt: IndexPath) -> Bool](./tableview%28_,shouldindentwhileeditingrowat%29.md)
  Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:editingstyleforrowat:))*