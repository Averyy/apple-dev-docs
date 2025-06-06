# showsReorderControl

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the cell shows the reordering control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsReorderControl: Bool { get set }
```

#### Discussion

The reordering control is gray, multiple horizontal bar control on the right side of the cell. Users can drag this control to reorder the cell within the table. The default value is [`false`](https://developer.apple.com/documentation/swift/false). If the value is [`true`](https://developer.apple.com/documentation/swift/true) , the reordering control temporarily replaces any accessory view.

For the reordering control to appear, you must not only set this property but implement the [`UITableViewDataSource`](uitableviewdatasource.md) method [`tableView(_:moveRowAt:to:)`](uitableviewdatasource/tableview(_:moverowat:to:).md). In addition, if the data source implements [`tableView(_:canMoveRowAt:)`](uitableviewdatasource/tableview(_:canmoverowat:).md) to return [`false`](https://developer.apple.com/documentation/swift/false), the reordering control doesn’t appear in that designated row.

## See Also

- [var isEditing: Bool](uitableviewcell/isediting.md)
  A Boolean value that indicates whether the cell is in an editable state.
- [func setEditing(Bool, animated: Bool)](uitableviewcell/setediting(_:animated:).md)
  Toggles the cell into and out of editing mode.
- [var editingStyle: UITableViewCell.EditingStyle](uitableviewcell/editingstyle-swift.property.md)
  The editing style of the cell.
- [UITableViewCell.EditingStyle](uitableviewcell/editingstyle-swift.enum.md)
  The editing control used by a cell.
- [var showingDeleteConfirmation: Bool](uitableviewcell/showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/showsreordercontrol)*