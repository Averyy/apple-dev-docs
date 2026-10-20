# UITableViewCell.EditingStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The editing control used by a cell.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum EditingStyle
```

```c
enum UITableViewCellEditingStyle : NSInteger;
```

#### Overview

Use these constants with the [`editingStyle`](./editingstyle-swift.property.md) property.

## Topics

### Constants
- [UITableViewCell.EditingStyle.none](./editingstyle-swift.enum/none.md)
  The cell has no editing control.
- [UITableViewCell.EditingStyle.delete](./editingstyle-swift.enum/delete.md)
  The cell has the delete editing control; this control is a red circle enclosing a minus sign.
- [UITableViewCell.EditingStyle.insert](./editingstyle-swift.enum/insert.md)
  The cell has the insert editing control; this control is a green circle enclosing a plus sign.
### Initializers
- [init?(rawValue: Int)](./editingstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Editing the cell
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the cell is in an editable state.
- [func setEditing(Bool, animated: Bool)](./setediting%28_,animated%29.md)
  Toggles the cell into and out of editing mode.
- [var editingStyle: UITableViewCell.EditingStyle](./editingstyle-swift.property.md)
  The editing style of the cell.
- [var showingDeleteConfirmation: Bool](./showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [var showsReorderControl: Bool](./showsreordercontrol.md)
  A Boolean value that determines whether the cell shows the reordering control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/editingstyle-swift.enum)*