# editingStyle

**Framework**: UIKit  
**Kind**: property

The editing style of the cell.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var editingStyle: UITableViewCell.EditingStyle { get }
```

#### Discussion

One of the constants described in [`UITableViewCell.EditingStyle`](uitableviewcell/editingstyle-swift.enum.md) is used as the value of this property; it specifies whether the cell is in an editable state and, if it is, whether it shows an insertion or deletion control. The default value is [`UITableViewCell.EditingStyle.none`](uitableviewcell/editingstyle-swift.enum/none.md) (not editable). The delegate returns the value of this property for a particular cell in its implementation of the [`tableView(_:editingStyleForRowAt:)`](uitableviewdelegate/tableview(_:editingstyleforrowat:).md) method.

## See Also

- [var isEditing: Bool](uitableviewcell/isediting.md)
  A Boolean value that indicates whether the cell is in an editable state.
- [func setEditing(Bool, animated: Bool)](uitableviewcell/setediting(_:animated:).md)
  Toggles the cell into and out of editing mode.
- [UITableViewCell.EditingStyle](uitableviewcell/editingstyle-swift.enum.md)
  The editing control used by a cell.
- [var showingDeleteConfirmation: Bool](uitableviewcell/showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [var showsReorderControl: Bool](uitableviewcell/showsreordercontrol.md)
  A Boolean value that determines whether the cell shows the reordering control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/editingstyle-swift.property)*