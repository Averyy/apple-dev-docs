# moveSection(_:toSection:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Moves a section to a new location in the table view.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func moveSection(_ section: Int, toSection newSection: Int)
```

```objc
- (void) moveSection:(NSInteger) section toSection:(NSInteger) newSection;
```

#### Discussion

You can combine section-move operations with section-insertion and section-deletion operations within a [`beginUpdates()`](./beginupdates%28%29.md)–[`endUpdates()`](./endupdates%28%29.md) block to have all changes occur together as a single animation.

Unlike the section-insertion section row-deletion methods, this method doesn’t take an animation parameter. For sections that are moved, the moved section animates straight from the starting position to the ending position. Also unlike the other methods, this method allows only one section to be moved per call. If you want multiple section moved, call this method repeatedly within a [`beginUpdates()`](./beginupdates%28%29.md)–[`endUpdates()`](./endupdates%28%29.md) block.

## Parameters

- `section`: The index of the section to move.
- `newSection`: The index in the table view that’s the destination of the move for the section. The existing section at that location slides up or down to an adjoining index position to make room for it.

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
- [UITableView.RowAnimation](./rowanimation.md)
  The type of animation to use when inserting or deleting rows.
- [func moveRow(at: IndexPath, to: IndexPath)](./moverow%28at,to%29.md)
  Moves the row at a specified location to a destination location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/movesection(_:tosection:))*