# reconfigureRows(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func reconfigureRows(at indexPaths: [IndexPath])
```

```objc
- (void) reconfigureRowsAtIndexPaths:(NSArray<NSIndexPath *> *) indexPaths;
```

#### Discussion

To update the contents of existing (including prefetched) cells without replacing them with new cells, use this method instead of [`reloadRows(at:with:)`](./reloadrows%28at,with%29.md). For optimal performance, choose to reconfigure rows instead of reloading rows unless you have an explicit need to replace the existing cell with a new cell.

Your cell provider must dequeue the same type of cell for the provided index path, and must return the same existing cell for a given index path. Because this method reconfigures existing cells, the table view doesn’t call [`prepareForReuse()`](../uitableviewcell/prepareforreuse%28%29.md) for each cell dequeued. If you need to return a different type of cell for an index path, use [`reloadRows(at:with:)`](./reloadrows%28at,with%29.md) instead.

If your cells are self-sizing, the table view resizes your cells after reconfiguring them.

By default, the table view animates any size or layout changes that are a result of reconfiguration. To reconfigure cells without animation, use `UIView`’s [`performWithoutAnimation(_:)`](../uiview/performwithoutanimation%28_%29.md) when you call this method. Alternatively, to avoid animations when setting specific properties, use [`performWithoutAnimation(_:)`](../uiview/performwithoutanimation%28_%29.md) in your cell configuration logic.

If your table view uses a custom implementation of `UITableViewDataSource`, use this method. If your table view uses a diffable data source, use [`reconfigureItems(_:)`](../nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems%28_%29.md) (Swift) or [`reconfigureItems(withIdentifiers:)`](../nsdiffabledatasourcesnapshotreference/reconfigureitems%28withidentifiers%29.md) (Objective-C) on `NSDiffableDataSourceSnapshot` instead.

## Parameters

- `indexPaths`: An array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects identifying the items you want to update.

## See Also

### Reloading the table view
- [var hasUncommittedUpdates: Bool](./hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads the rows and sections of the table view.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](./reloadrows%28at,with%29.md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSections(IndexSet, with: UITableView.RowAnimation)](./reloadsections%28_,with%29.md)
  Reloads the specified sections using the provided animation effect.
- [func reloadSectionIndexTitles()](./reloadsectionindextitles%28%29.md)
  Reloads the items in the index bar along the right side of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/reconfigurerows(at:))*