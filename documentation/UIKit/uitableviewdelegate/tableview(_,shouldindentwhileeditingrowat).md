# tableView(_:shouldIndentWhileEditingRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, shouldIndentWhileEditingRowAt indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView shouldIndentWhileEditingRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

[`true`](../../Swift/true.md) if the background of the row should be indented, otherwise [`false`](../../Swift/false.md).

## Discussion

If the delegate does not implement this method, the default is [`true`](../../Swift/true.md). This method is unrelated to [`tableView(_:indentationLevelForRowAt:)`](./tableview%28_,indentationlevelforrowat%29.md).

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path locating the row in its section.

## See Also

### Editing table rows
- [func tableView(UITableView, willBeginEditingRowAt: IndexPath)](./tableview%28_,willbegineditingrowat%29.md)
  Tells the delegate that the table view is about to go into editing mode.
- [func tableView(UITableView, didEndEditingRowAt: IndexPath?)](./tableview%28_,didendeditingrowat%29.md)
  Tells the delegate that the table view has left editing mode.
- [func tableView(UITableView, editingStyleForRowAt: IndexPath) -> UITableViewCell.EditingStyle](./tableview%28_,editingstyleforrowat%29.md)
  Asks the delegate for the editing style of a row at a particular location in a table view.
- [func tableView(UITableView, titleForDeleteConfirmationButtonForRowAt: IndexPath) -> String?](./tableview%28_,titlefordeleteconfirmationbuttonforrowat%29.md)
  Changes the default title of the delete-confirmation button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldindentwhileeditingrowat:))*