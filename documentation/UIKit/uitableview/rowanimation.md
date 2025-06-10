# UITableView.RowAnimation

**Framework**: UIKit  
**Kind**: enum

The type of animation to use when inserting or deleting rows.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum RowAnimation
```

#### Overview

You specify one of these constants as a parameter of the [`insertRows(at:with:)`](uitableview/insertrows(at:with:).md), [`insertSections(_:with:)`](uitableview/insertsections(_:with:).md), [`deleteRows(at:with:)`](uitableview/deleterows(at:with:).md),[`deleteSections(_:with:)`](uitableview/deletesections(_:with:).md), [`reloadRows(at:with:)`](uitableview/reloadrows(at:with:).md), and [`reloadSections(_:with:)`](uitableview/reloadsections(_:with:).md) methods.

## Topics

### Constants
- [UITableView.RowAnimation.fade](uitableview/rowanimation/fade.md)
  The inserted or deleted row or rows fade into or out of the table view.
- [UITableView.RowAnimation.right](uitableview/rowanimation/right.md)
  The inserted row or rows slide in from the right; the deleted row or rows slide out to the right.
- [UITableView.RowAnimation.left](uitableview/rowanimation/left.md)
  The inserted row or rows slide in from the left; the deleted row or rows slide out to the left.
- [UITableView.RowAnimation.top](uitableview/rowanimation/top.md)
  The inserted row or rows slide in from the top; the deleted row or rows slide out toward the top.
- [UITableView.RowAnimation.bottom](uitableview/rowanimation/bottom.md)
  The inserted row or rows slide in from the bottom; the deleted row or rows slide out toward the bottom.
- [UITableView.RowAnimation.none](uitableview/rowanimation/none.md)
  The inserted or deleted rows use the default animations.
- [UITableView.RowAnimation.middle](uitableview/rowanimation/middle.md)
  The table view attempts to keep the old and new cells centered in the space they did or will occupy.
- [UITableView.RowAnimation.automatic](uitableview/rowanimation/automatic.md)
  The table view chooses an appropriate animation style for you.
### Initializers
- [init?(rawValue: Int)](uitableview/rowanimation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func insertRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/insertrows(at:with:).md)
  Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [func deleteRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/deleterows(at:with:).md)
  Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [func insertSections(IndexSet, with: UITableView.RowAnimation)](uitableview/insertsections(_:with:).md)
  Inserts one or more sections in the table view, with an option to animate the insertion.
- [func deleteSections(IndexSet, with: UITableView.RowAnimation)](uitableview/deletesections(_:with:).md)
  Deletes one or more sections in the table view, with an option to animate the deletion.
- [func moveRow(at: IndexPath, to: IndexPath)](uitableview/moverow(at:to:).md)
  Moves the row at a specified location to a destination location.
- [func moveSection(Int, toSection: Int)](uitableview/movesection(_:tosection:).md)
  Moves a section to a new location in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/rowanimation)*