# UITableViewCell.EditingStyle

**Framework**: UIKit  
**Kind**: enum

The editing control used by a cell.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum EditingStyle
```

#### Overview

Use these constants with the [`editingStyle`](uitableviewcell/editingstyle-swift.property.md) property.

## Topics

### Constants
- [UITableViewCell.EditingStyle.none](uitableviewcell/editingstyle-swift.enum/none.md)
  The cell has no editing control.
- [UITableViewCell.EditingStyle.delete](uitableviewcell/editingstyle-swift.enum/delete.md)
  The cell has the delete editing control; this control is a red circle enclosing a minus sign.
- [UITableViewCell.EditingStyle.insert](uitableviewcell/editingstyle-swift.enum/insert.md)
  The cell has the insert editing control; this control is a green circle enclosing a plus sign.
### Initializers
- [init?(rawValue: Int)](uitableviewcell/editingstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isEditing: Bool](uitableviewcell/isediting.md)
  A Boolean value that indicates whether the cell is in an editable state.
- [func setEditing(Bool, animated: Bool)](uitableviewcell/setediting(_:animated:).md)
  Toggles the cell into and out of editing mode.
- [var editingStyle: UITableViewCell.EditingStyle](uitableviewcell/editingstyle-swift.property.md)
  The editing style of the cell.
- [var showingDeleteConfirmation: Bool](uitableviewcell/showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [var showsReorderControl: Bool](uitableviewcell/showsreordercontrol.md)
  A Boolean value that determines whether the cell shows the reordering control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/editingstyle-swift.enum)*