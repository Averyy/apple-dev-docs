# showingDeleteConfirmation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var showingDeleteConfirmation: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL showingDeleteConfirmation;
```

#### Discussion

When users tap the deletion control (the red circle to the left of the cell), the cell displays a “Delete” button on the right side of the cell; this string is localized.

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
- [var showsReorderControl: Bool](./showsreordercontrol.md)
  A Boolean value that determines whether the cell shows the reordering control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/showingdeleteconfirmation)*