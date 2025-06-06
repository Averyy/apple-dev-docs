# moveRow(at:to:)

**Framework**: UIKit  
**Kind**: method

Moves the row at a specified location to a destination location.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func moveRow(at indexPath: IndexPath, to newIndexPath: IndexPath)
```

#### Discussion

You can combine row-move operations with row-insertion and row-deletion operations within a [`beginUpdates()`](uitableview/beginupdates().md)–[`endUpdates()`](uitableview/endupdates().md) block to have all changes occur together as a single animation.

Unlike the row-insertion and row-deletion methods, this method doesn’t take an `animation` parameter. For rows that are moved, the moved row animates straight from the starting position to the ending position. Also unlike the other methods, this method allows only one row to be moved per call. If you want multiple rows moved, you can call this method repeatedly within a [`beginUpdates()`](uitableview/beginupdates().md)–[`endUpdates()`](uitableview/endupdates().md) block.

## Parameters

- `indexPath`: An index path identifying the row to move.
- `newIndexPath`: An index path identifying the row that’s the destination of the row at  . The existing row at that location slides up or down to an adjoining index position to make room for it.

## See Also

- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/reloadrows(at:with:).md)
  Reloads the specified rows using the provided animation effect.
- [func insertRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/insertrows(at:with:).md)
  Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [func deleteRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/deleterows(at:with:).md)
  Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [func insertSections(IndexSet, with: UITableView.RowAnimation)](uitableview/insertsections(_:with:).md)
  Inserts one or more sections in the table view, with an option to animate the insertion.
- [func deleteSections(IndexSet, with: UITableView.RowAnimation)](uitableview/deletesections(_:with:).md)
  Deletes one or more sections in the table view, with an option to animate the deletion.
- [UITableView.RowAnimation](uitableview/rowanimation.md)
  The type of animation to use when inserting or deleting rows.
- [func moveSection(Int, toSection: Int)](uitableview/movesection(_:tosection:).md)
  Moves a section to a new location in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/moverow(at:to:))*