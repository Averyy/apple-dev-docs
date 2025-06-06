# tableView(_:shouldIndentWhileEditingRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, shouldIndentWhileEditingRowAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the background of the row should be indented, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the delegate does not implement this method, the default is [`true`](https://developer.apple.com/documentation/swift/true). This method is unrelated to [`tableView(_:indentationLevelForRowAt:)`](uitableviewdelegate/tableview(_:indentationlevelforrowat:).md).

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path locating the row in its section.

## See Also

- [func tableView(UITableView, willBeginEditingRowAt: IndexPath)](uitableviewdelegate/tableview(_:willbegineditingrowat:).md)
  Tells the delegate that the table view is about to go into editing mode.
- [func tableView(UITableView, didEndEditingRowAt: IndexPath?)](uitableviewdelegate/tableview(_:didendeditingrowat:).md)
  Tells the delegate that the table view has left editing mode.
- [func tableView(UITableView, editingStyleForRowAt: IndexPath) -> UITableViewCell.EditingStyle](uitableviewdelegate/tableview(_:editingstyleforrowat:).md)
  Asks the delegate for the editing style of a row at a particular location in a table view.
- [func tableView(UITableView, titleForDeleteConfirmationButtonForRowAt: IndexPath) -> String?](uitableviewdelegate/tableview(_:titlefordeleteconfirmationbuttonforrowat:).md)
  Changes the default title of the delete-confirmation button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldindentwhileeditingrowat:))*