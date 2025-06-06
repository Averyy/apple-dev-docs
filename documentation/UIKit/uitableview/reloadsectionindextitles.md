# reloadSectionIndexTitles()

**Framework**: UIKit  
**Kind**: method

Reloads the items in the index bar along the right side of the table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reloadSectionIndexTitles()
```

#### Discussion

This method gives you a way to update the section index after inserting or deleting sections without having to reload the whole table.

## See Also

- [func sectionIndexTitles(for: UITableView) -> [String]?](uitableviewdatasource/sectionindextitles(for:).md)
  Asks the data source to return the titles for the sections of a table view.
- [var hasUncommittedUpdates: Bool](uitableview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reconfigureRows(at: [IndexPath])](uitableview/reconfigurerows(at:).md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadData()](uitableview/reloaddata.md)
  Reloads the rows and sections of the table view.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/reloadrows(at:with:).md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSections(IndexSet, with: UITableView.RowAnimation)](uitableview/reloadsections(_:with:).md)
  Reloads the specified sections using the provided animation effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/reloadsectionindextitles())*