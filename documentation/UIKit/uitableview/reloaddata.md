# reloadData()

**Framework**: UIKit  
**Kind**: method

Reloads the rows and sections of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reloadData()
```

#### Discussion

Call this method to reload all the data that’s used to construct the table, including cells, section headers and footers, index arrays, and so on. For efficiency, the table view redisplays only those rows that are visible. It adjusts offsets if the table shrinks as a result of the reload. The table view’s delegate or data source calls this method when it wants the table view to completely reload its data. It shouldn’t be called in the methods that insert or delete rows, especially within an animation block implemented with calls to [`beginUpdates()`](uitableview/beginupdates().md) and [`endUpdates()`](uitableview/endupdates().md).

> ❗ **Important**:  Don’t call this method when the [`hasUncommittedUpdates`](uitableview/hasuncommittedupdates.md) property is [`true`](https://developer.apple.com/documentation/swift/true). Doing so forces the table view to delete any uncommitted changes before reloading the data.

 Don’t call this method when the [`hasUncommittedUpdates`](uitableview/hasuncommittedupdates.md) property is [`true`](https://developer.apple.com/documentation/swift/true). Doing so forces the table view to delete any uncommitted changes before reloading the data.

## See Also

- [var hasUncommittedUpdates: Bool](uitableview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reconfigureRows(at: [IndexPath])](uitableview/reconfigurerows(at:).md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/reloadrows(at:with:).md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSections(IndexSet, with: UITableView.RowAnimation)](uitableview/reloadsections(_:with:).md)
  Reloads the specified sections using the provided animation effect.
- [func reloadSectionIndexTitles()](uitableview/reloadsectionindextitles.md)
  Reloads the items in the index bar along the right side of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/reloaddata())*