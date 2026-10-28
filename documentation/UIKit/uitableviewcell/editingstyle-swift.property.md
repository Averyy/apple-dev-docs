# editingStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The editing style of the cell.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var editingStyle: UITableViewCell.EditingStyle { get }
```

```objc
@property (nonatomic, readonly) UITableViewCellEditingStyle editingStyle;
```

## Discussion

One of the constants described in [`UITableViewCell.EditingStyle`](./editingstyle-swift.enum.md) is used as the value of this property; it specifies whether the cell is in an editable state and, if it is, whether it shows an insertion or deletion control. The default value is [`UITableViewCell.EditingStyle.none`](./editingstyle-swift.enum/none.md) (not editable). The delegate returns the value of this property for a particular cell in its implementation of the [`tableView(_:editingStyleForRowAt:)`](../uitableviewdelegate/tableview%28_,editingstyleforrowat%29.md) method.

## See Also

### Editing the cell
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the cell is in an editable state.
- [func setEditing(Bool, animated: Bool)](./setediting%28_,animated%29.md)
  Toggles the cell into and out of editing mode.
- [UITableViewCell.EditingStyle](./editingstyle-swift.enum.md)
  The editing control used by a cell.
- [var showingDeleteConfirmation: Bool](./showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [var showsReorderControl: Bool](./showsreordercontrol.md)
  A Boolean value that determines whether the cell shows the reordering control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/editingstyle-swift.property)*