# showsReorderControl

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the cell shows the reordering control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var showsReorderControl: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsReorderControl;
```

#### Discussion

The reordering control is gray, multiple horizontal bar control on the right side of the cell. Users can drag this control to reorder the cell within the table. The default value is [`false`](../../Swift/false.md). If the value is [`true`](../../Swift/true.md) , the reordering control temporarily replaces any accessory view.

For the reordering control to appear, you must not only set this property but implement the [`UITableViewDataSource`](../uitableviewdatasource.md) method [`tableView(_:moveRowAt:to:)`](../uitableviewdatasource/tableview%28_,moverowat,to%29.md). In addition, if the data source implements [`tableView(_:canMoveRowAt:)`](../uitableviewdatasource/tableview%28_,canmoverowat%29.md) to return [`false`](../../Swift/false.md), the reordering control doesn’t appear in that designated row.

## See Also

### Editing the cell
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the cell is in an editable state.
- [func setEditing(Bool, animated: Bool)](./setediting%28_,animated%29.md)
  Toggles the cell into and out of editing mode.
- [var editingStyle: UITableViewCell.EditingStyle](./editingstyle-swift.property.md)
  The editing style of the cell.
- [UITableViewCell.EditingStyle](./editingstyle-swift.enum.md)
  The editing control used by a cell.
- [var showingDeleteConfirmation: Bool](./showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/showsreordercontrol)*