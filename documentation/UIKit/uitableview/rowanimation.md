# UITableView.RowAnimation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The type of animation to use when inserting or deleting rows.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum RowAnimation
```

```c
enum UITableViewRowAnimation : NSInteger;
```

#### Overview

You specify one of these constants as a parameter of the [`insertRows(at:with:)`](./insertrows%28at,with%29.md), [`insertSections(_:with:)`](./insertsections%28_,with%29.md), [`deleteRows(at:with:)`](./deleterows%28at,with%29.md),[`deleteSections(_:with:)`](./deletesections%28_,with%29.md), [`reloadRows(at:with:)`](./reloadrows%28at,with%29.md), and [`reloadSections(_:with:)`](./reloadsections%28_,with%29.md) methods.

## Topics

### Constants
- [UITableView.RowAnimation.fade](./rowanimation/fade.md)
  The inserted or deleted row or rows fade into or out of the table view.
- [UITableView.RowAnimation.right](./rowanimation/right.md)
  The inserted row or rows slide in from the right; the deleted row or rows slide out to the right.
- [UITableView.RowAnimation.left](./rowanimation/left.md)
  The inserted row or rows slide in from the left; the deleted row or rows slide out to the left.
- [UITableView.RowAnimation.top](./rowanimation/top.md)
  The inserted row or rows slide in from the top; the deleted row or rows slide out toward the top.
- [UITableView.RowAnimation.bottom](./rowanimation/bottom.md)
  The inserted row or rows slide in from the bottom; the deleted row or rows slide out toward the bottom.
- [UITableView.RowAnimation.none](./rowanimation/none.md)
  The inserted or deleted rows use the default animations.
- [UITableView.RowAnimation.middle](./rowanimation/middle.md)
  The table view attempts to keep the old and new cells centered in the space they did or will occupy.
- [UITableView.RowAnimation.automatic](./rowanimation/automatic.md)
  The table view chooses an appropriate animation style for you.
### Initializers
- [init?(rawValue: Int)](./rowanimation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inserting, deleting, and moving rows and sections
- [func insertRows(at: [IndexPath], with: UITableView.RowAnimation)](./insertrows%28at,with%29.md)
  Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [func deleteRows(at: [IndexPath], with: UITableView.RowAnimation)](./deleterows%28at,with%29.md)
  Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [func insertSections(IndexSet, with: UITableView.RowAnimation)](./insertsections%28_,with%29.md)
  Inserts one or more sections in the table view, with an option to animate the insertion.
- [func deleteSections(IndexSet, with: UITableView.RowAnimation)](./deletesections%28_,with%29.md)
  Deletes one or more sections in the table view, with an option to animate the deletion.
- [func moveRow(at: IndexPath, to: IndexPath)](./moverow%28at,to%29.md)
  Moves the row at a specified location to a destination location.
- [func moveSection(Int, toSection: Int)](./movesection%28_,tosection%29.md)
  Moves a section to a new location in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/rowanimation)*