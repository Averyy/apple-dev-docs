# isEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the cell is in an editable state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isEditing: Bool { get set }
```

```objc
@property (nonatomic, getter=isEditing) BOOL editing;
```

#### Discussion

When a cell is in an editable state, it displays the editing controls specified for it: the green insertion control, the red deletion control, or (on the right side) the reordering control. Use [`editingStyle`](./editingstyle-swift.property.md) and [`showsReorderControl`](./showsreordercontrol.md) to specify these controls for the cell.

## See Also

### Editing the cell
- [func setEditing(Bool, animated: Bool)](./setediting%28_,animated%29.md)
  Toggles the cell into and out of editing mode.
- [var editingStyle: UITableViewCell.EditingStyle](./editingstyle-swift.property.md)
  The editing style of the cell.
- [UITableViewCell.EditingStyle](./editingstyle-swift.enum.md)
  The editing control used by a cell.
- [var showingDeleteConfirmation: Bool](./showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [var showsReorderControl: Bool](./showsreordercontrol.md)
  A Boolean value that determines whether the cell shows the reordering control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/isediting)*