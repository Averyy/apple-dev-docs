# moveRow(at:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Moves the row at a specified location to a destination location.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func moveRow(at indexPath: IndexPath, to newIndexPath: IndexPath)
```

```objc
- (void) moveRowAtIndexPath:(NSIndexPath *) indexPath toIndexPath:(NSIndexPath *) newIndexPath;
```

#### Discussion

You can combine row-move operations with row-insertion and row-deletion operations within a [`beginUpdates()`](./beginupdates%28%29.md)–[`endUpdates()`](./endupdates%28%29.md) block to have all changes occur together as a single animation.

Unlike the row-insertion and row-deletion methods, this method doesn’t take an `animation` parameter. For rows that are moved, the moved row animates straight from the starting position to the ending position. Also unlike the other methods, this method allows only one row to be moved per call. If you want multiple rows moved, you can call this method repeatedly within a [`beginUpdates()`](./beginupdates%28%29.md)–[`endUpdates()`](./endupdates%28%29.md) block.

## Parameters

- `indexPath`: An index path identifying the row to move.
- `newIndexPath`: An index path identifying the row that’s the destination of the row at `indexPath`. The existing row at that location slides up or down to an adjoining index position to make room for it.

## See Also

### Related Documentation
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](./reloadrows%28at,with%29.md)
  Reloads the specified rows using the provided animation effect.
### Inserting, deleting, and moving rows and sections
- [func insertRows(at: [IndexPath], with: UITableView.RowAnimation)](./insertrows%28at,with%29.md)
  Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [func deleteRows(at: [IndexPath], with: UITableView.RowAnimation)](./deleterows%28at,with%29.md)
  Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [func insertSections(IndexSet, with: UITableView.RowAnimation)](./insertsections%28_,with%29.md)
  Inserts one or more sections in the table view, with an option to animate the insertion.
- [func deleteSections(IndexSet, with: UITableView.RowAnimation)](./deletesections%28_,with%29.md)
  Deletes one or more sections in the table view, with an option to animate the deletion.
- [UITableView.RowAnimation](./rowanimation.md)
  The type of animation to use when inserting or deleting rows.
- [func moveSection(Int, toSection: Int)](./movesection%28_,tosection%29.md)
  Moves a section to a new location in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/moverow(at:to:))*