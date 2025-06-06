# deselectRow(at:animated:)

**Framework**: UIKit  
**Kind**: method

Deselects a row that an index path identifies, with an option to animate the deselection.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func deselectRow(at indexPath: IndexPath, animated: Bool)
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Discussion

Calling this method doesn’t cause the delegate to receive a [`tableView(_:willDeselectRowAt:)`](uitableviewdelegate/tableview(_:willdeselectrowat:).md) or [`tableView(_:didDeselectRowAt:)`](uitableviewdelegate/tableview(_:diddeselectrowat:).md) message, nor does it send [`selectionDidChangeNotification`](uitableview/selectiondidchangenotification.md) notifications to observers.

Calling this method doesn’t cause any scrolling to the deselected row.

## Parameters

- `indexPath`: An index path identifying a row in the table view.
- `animated`:   if you want to animate the deselection, and   if the change should be immediate.

## See Also

- [var indexPathForSelectedRow: IndexPath?](uitableview/indexpathforselectedrow.md)
  An index path that identifies the row and section of the selected row.
- [var indexPathsForSelectedRows: [IndexPath]?](uitableview/indexpathsforselectedrows.md)
  The index paths that represent the selected rows.
- [func selectRow(at: IndexPath?, animated: Bool, scrollPosition: UITableView.ScrollPosition)](uitableview/selectrow(at:animated:scrollposition:).md)
  Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
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
- [class let selectionDidChangeNotification: NSNotification.Name](uitableview/selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/deselectrow(at:animated:))*