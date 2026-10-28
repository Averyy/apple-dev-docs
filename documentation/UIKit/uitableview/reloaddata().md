# reloadData()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the rows and sections of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func reloadData()
```

```objc
- (void) reloadData;
```

## Discussion

Call this method to reload all the data that’s used to construct the table, including cells, section headers and footers, index arrays, and so on. For efficiency, the table view redisplays only those rows that are visible. It adjusts offsets if the table shrinks as a result of the reload. The table view’s delegate or data source calls this method when it wants the table view to completely reload its data. It shouldn’t be called in the methods that insert or delete rows, especially within an animation block implemented with calls to [`beginUpdates()`](./beginupdates%28%29.md) and [`endUpdates()`](./endupdates%28%29.md).

> ❗ **Important**:  Don’t call this method when the [`hasUncommittedUpdates`](./hasuncommittedupdates.md) property is [`true`](../../Swift/true.md). Doing so forces the table view to delete any uncommitted changes before reloading the data.

## See Also

### Reloading the table view
- [var hasUncommittedUpdates: Bool](./hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reconfigureRows(at: [IndexPath])](./reconfigurerows%28at%29.md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](./reloadrows%28at,with%29.md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSections(IndexSet, with: UITableView.RowAnimation)](./reloadsections%28_,with%29.md)
  Reloads the specified sections using the provided animation effect.
- [func reloadSectionIndexTitles()](./reloadsectionindextitles%28%29.md)
  Reloads the items in the index bar along the right side of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/reloaddata())*