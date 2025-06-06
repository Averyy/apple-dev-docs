# reloadSections(_:with:)

**Framework**: UIKit  
**Kind**: method

Reloads the specified sections using the provided animation effect.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reloadSections(_ sections: IndexSet, with animation: UITableView.RowAnimation)
```

#### Discussion

Calling this method causes the table view to ask its data source for new cells for the specified sections. The table view animates the insertion of new cells in as it animates the old cells out. Call this method if you want to alert the user that the values of the designated sections are changing. If, however, you just want to change values in cells of the specified sections without alerting the user, you can get those cells and directly set their new values.

When this method is called in an animation block defined by the [`beginUpdates()`](uitableview/beginupdates().md) and [`endUpdates()`](uitableview/endupdates().md) methods, it behaves similarly to [`deleteSections(_:with:)`](uitableview/deletesections(_:with:).md). The indexes that `UITableView` passes to the method are specified in the state of the table view prior to any updates. This happens regardless of ordering of the insertion, deletion, and reloading method calls within the animation block.

## Parameters

- `sections`: An index set identifying the sections to reload.
- `animation`: The animation constant affects the direction in which both the old and the new section rows slide. For example, if the animation constant is  , the old rows slide out to the right and the new cells slide in from the right.

## See Also

- [func insertSections(IndexSet, with: UITableView.RowAnimation)](uitableview/insertsections(_:with:).md)
  Inserts one or more sections in the table view, with an option to animate the insertion.
- [var hasUncommittedUpdates: Bool](uitableview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reconfigureRows(at: [IndexPath])](uitableview/reconfigurerows(at:).md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadData()](uitableview/reloaddata.md)
  Reloads the rows and sections of the table view.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/reloadrows(at:with:).md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSectionIndexTitles()](uitableview/reloadsectionindextitles.md)
  Reloads the items in the index bar along the right side of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/reloadsections(_:with:))*