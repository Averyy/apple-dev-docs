# selectionDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when the selected row in the posting table view changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
nonisolated
class let selectionDidChangeNotification: NSNotification.Name
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Discussion

There’s no `userInfo` dictionary associated with this notification.

## See Also

- [var indexPathForSelectedRow: IndexPath?](uitableview/indexpathforselectedrow.md)
  An index path that identifies the row and section of the selected row.
- [var indexPathsForSelectedRows: [IndexPath]?](uitableview/indexpathsforselectedrows.md)
  The index paths that represent the selected rows.
- [func selectRow(at: IndexPath?, animated: Bool, scrollPosition: UITableView.ScrollPosition)](uitableview/selectrow(at:animated:scrollposition:).md)
  Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
- [func deselectRow(at: IndexPath, animated: Bool)](uitableview/deselectrow(at:animated:).md)
  Deselects a row that an index path identifies, with an option to animate the deselection.
- [var allowsSelection: Bool](uitableview/allowsselection.md)
  A Boolean value that determines whether users can select a row.
- [var allowsMultipleSelection: Bool](uitableview/allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one row outside of editing mode.
- [var allowsSelectionDuringEditing: Bool](uitableview/allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](uitableview/allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](uitableview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/selectiondidchangenotification)*