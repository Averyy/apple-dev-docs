# deleteRows(at:with:)

**Framework**: UIKit  
**Kind**: method

Deletes the rows that an array of index paths identifies, with an option to animate the deletion.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func deleteRows(at indexPaths: [IndexPath], with animation: UITableView.RowAnimation)
```

#### Discussion

When this method is called in an animation block defined by the [`beginUpdates()`](uitableview/beginupdates().md) and [`endUpdates()`](uitableview/endupdates().md) methods, `UITableView` defers any insertions of rows or sections until after it has handled the deletions of rows or sections. This order is followed regardless how the insertion and deletion method calls are ordered. This is unlike inserting or removing an item in a mutable array, in which the operation can affect the array index used for the successive insertion or removal operation. For more on this subject, see [`Batch Insertion, Deletion, and Reloading of Rows and Sections`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/ManageInsertDeleteRow/ManageInsertDeleteRow.html#//apple_ref/doc/uid/TP40007451-CH10-SW9) in [`Table View Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451).

## Parameters

- `indexPaths`: An array of   objects identifying the rows to delete.
- `animation`: A constant that indicates how the deletion is to be animated, for example, fade out or slide out from the bottom. See   for descriptions of these constants.

## See Also

- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/reloadrows(at:with:).md)
  Reloads the specified rows using the provided animation effect.
- [func insertRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/insertrows(at:with:).md)
  Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [func insertSections(IndexSet, with: UITableView.RowAnimation)](uitableview/insertsections(_:with:).md)
  Inserts one or more sections in the table view, with an option to animate the insertion.
- [func deleteSections(IndexSet, with: UITableView.RowAnimation)](uitableview/deletesections(_:with:).md)
  Deletes one or more sections in the table view, with an option to animate the deletion.
- [UITableView.RowAnimation](uitableview/rowanimation.md)
  The type of animation to use when inserting or deleting rows.
- [func moveRow(at: IndexPath, to: IndexPath)](uitableview/moverow(at:to:).md)
  Moves the row at a specified location to a destination location.
- [func moveSection(Int, toSection: Int)](uitableview/movesection(_:tosection:).md)
  Moves a section to a new location in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/deleterows(at:with:))*