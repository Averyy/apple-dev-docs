# hasUncommittedUpdates

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var hasUncommittedUpdates: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasUncommittedUpdates;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the table view contains placeholder cells or is handling a drop and is in the middle of reordering its rows. When this property is [`true`](../../Swift/true.md), avoid making any significant changes to the table view. Specifically, don’t call [`reloadData()`](./reloaddata%28%29.md), which forces the table to delete any uncommitted changes before retrieving fresh data from the data source object.

## See Also

### Reloading the table view
- [func reconfigureRows(at: [IndexPath])](./reconfigurerows%28at%29.md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads the rows and sections of the table view.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](./reloadrows%28at,with%29.md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSections(IndexSet, with: UITableView.RowAnimation)](./reloadsections%28_,with%29.md)
  Reloads the specified sections using the provided animation effect.
- [func reloadSectionIndexTitles()](./reloadsectionindextitles%28%29.md)
  Reloads the items in the index bar along the right side of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/hasuncommittedupdates)*