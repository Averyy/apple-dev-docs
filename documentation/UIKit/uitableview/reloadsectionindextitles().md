# reloadSectionIndexTitles()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the items in the index bar along the right side of the table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func reloadSectionIndexTitles()
```

```objc
- (void) reloadSectionIndexTitles;
```

#### Discussion

This method gives you a way to update the section index after inserting or deleting sections without having to reload the whole table.

## See Also

### Related Documentation
- [func sectionIndexTitles(for: UITableView) -> [String]?](../uitableviewdatasource/sectionindextitles%28for%29.md)
  Asks the data source to return the titles for the sections of a table view.
### Reloading the table view
- [var hasUncommittedUpdates: Bool](./hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reconfigureRows(at: [IndexPath])](./reconfigurerows%28at%29.md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads the rows and sections of the table view.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](./reloadrows%28at,with%29.md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSections(IndexSet, with: UITableView.RowAnimation)](./reloadsections%28_,with%29.md)
  Reloads the specified sections using the provided animation effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/reloadsectionindextitles())*