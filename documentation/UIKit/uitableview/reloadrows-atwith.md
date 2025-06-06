# reloadRows(at:with:)

**Framework**: UIKit  
**Kind**: method

Reloads the specified rows using the provided animation effect.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reloadRows(at indexPaths: [IndexPath], with animation: UITableView.RowAnimation)
```

#### Discussion

Reloading a row causes the table view to ask its data source for a new cell for that row. The table animates that new cell in as it animates the old row out. Call this method if you want to alert the user that the value of a cell is changing. If, however, notifying the user isn’t important — that is, you just want to change the value that a cell is displaying — you can get the cell for a particular row and set its new value.

When this method is called in an animation block defined by the [`beginUpdates()`](uitableview/beginupdates().md) and [`endUpdates()`](uitableview/endupdates().md) methods, it behaves similarly to [`deleteRows(at:with:)`](uitableview/deleterows(at:with:).md). The indexes that [`UITableView`](uitableview.md) passes to the method are specified in the state of the table view prior to any updates. This happens regardless of ordering of the insertion, deletion, and reloading method calls within the animation block.

## Parameters

- `indexPaths`: An array of   objects identifying the rows to reload.
- `animation`: The animation constant affects the direction in which both the old and the new rows slide. For example, if the animation constant is  , the old rows slide out to the right and the new cells slide in from the right.

## See Also

- [func insertRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/insertrows(at:with:).md)
  Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [var hasUncommittedUpdates: Bool](uitableview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reconfigureRows(at: [IndexPath])](uitableview/reconfigurerows(at:).md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadData()](uitableview/reloaddata.md)
  Reloads the rows and sections of the table view.
- [func reloadSections(IndexSet, with: UITableView.RowAnimation)](uitableview/reloadsections(_:with:).md)
  Reloads the specified sections using the provided animation effect.
- [func reloadSectionIndexTitles()](uitableview/reloadsectionindextitles.md)
  Reloads the items in the index bar along the right side of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/reloadrows(at:with:))*